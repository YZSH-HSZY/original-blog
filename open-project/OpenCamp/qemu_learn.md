# Learning Qemu Camp 2025

记录 2025 由格维开源社区(GTOC)主办的第一期 QEMU 训练营 QEMU 训练营学习笔记

> 相关文档:
- [qemu学习社区介绍](https://opencamp.cn/qemu/camp/2025/stage/4)
- [qemu专业手册](https://gevico.github.io/learning-qemu-docs/ch4/prof-level-manual/)

## 概念介绍

### Hypervisor(虚拟机监控器)

虚拟化的核心引擎，通过在硬件与操作系统之间插入抽象层，实现多虚拟机共存。

> 包括三大关键技术:
- `资源隔离`
- `敏感指令捕获`
- `内存虚拟化`

#### 资源隔离(Isolation)

- 空间分割
    * 内存隔离: 为每个虚拟机分配独立物理内存区域（或虚拟地址空间）
    * CPU 隔离: 时间片轮转调度 vCPU（如 Xen 的 Credit Scheduler）
- 硬件访问控制

### QOM(QEMU Object Model)

QEMU 使用面向对象思想实现的抽象层，用来组织 QEMU 中的各种组件（比如设备模拟、后端组件 MemoryRegion、Machine 等）。类似于 C++ 的类，但是 QOM 是用纯 C 语言来实现的。

> QOM 的运作过程包含三个部分: 类型的注册、类型的初始化、对象的初始化, 如下所示
```c
    |--类型注册     ---> type_init()
    |                   register_module_init()
    |                   type_register()
QOM-|--类型的初始化  ---> type_initialize()
    |--对象的初始化  ---> object_new()
    |                   object_initialize()
    |                   object_initialize_with_type()
```

> 基于面向对象的建模思想，QEMU 提供了一套非常格式化、套路化的硬件建模流程

#### 类型注册

以edu为示例
```c
// hw/miscs/edu.c
static void pci_edu_register_types(void)
{
    static InterfaceInfo interfaces[] = {
        { INTERFACE_CONVENTIONAL_PCI_DEVICE },
        { },
    };
    static const TypeInfo edu_info = {
        .name          = TYPE_PCI_EDU_DEVICE, // 定义类型的名称，一般用宏来定义一个字符串
        .parent        = TYPE_PCI_DEVICE,     // edu 的父类是 PCI Device
        .instance_size = sizeof(EduState),    // 获取 edu 对象的实例化大小，EduState 是一个结构体
        .instance_init = edu_instance_init,   // edu 对象的初始化接口
        .class_init    = edu_class_init,      // edu 类型的初始化函数
        .interfaces = interfaces,
    };

    type_register_static(&edu_info);          // 注册这个类型
}
type_init(pci_edu_register_types)

// include/qemu/module.h
#define type_init(function) module_init(function, MODULE_INIT_QOM)  // 模块注册

#ifdef BUILD_DSO
void DSO_STAMP_FUN(void);
/* This is a dummy symbol to identify a loaded DSO as a QEMU module, so we can
 * distinguish "version mismatch" from "not a QEMU module", when the stamp
 * check fails during module loading */
void qemu_module_dummy(void);

#define module_init(function, type)                                         \
static void __attribute__((constructor)) do_qemu_init_ ## function(void)    \
{                                                                           \
    register_dso_module_init(function, type);                               \
}
#else
/* This should not be used directly.  Use block_init etc. instead.  */
#define module_init(function, type)                                         \
static void __attribute__((constructor)) do_qemu_init_ ## function(void)    \
{                                                                           \
    register_module_init(function, type);                                   \
}
#endif

// utils/module.c

void register_module_init(void (*fn)(void), module_init_type type)
{
    ModuleEntry *e;
    ModuleTypeList *l;

    e = g_malloc0(sizeof(*e));
    e->init = fn;
    e->type = type;

    l = find_type(type);

    QTAILQ_INSERT_TAIL(l, e, node);
}
```
`type_init` 被扩展为一个在main执行之前调用的函数`do_qemu_init_##function`, 内部通过 `register_module_init()` 构建出一个 `ModuleEntry`(包含类型的初始化函数及所属类型`对于 QOM 类型来说是 MODULE_INIT_QOM`)，然后插入到对应 module 所属的链表中，所有 module 的链表存放在一个 `init_type_list` 数组中

`init_type_list` 结构类似如下:
```
               pci_edu_register_types                    
                     ^                                   
                     |      vmxnet3_register_types       
                     |           ^                       
                     +---+       |    intc_register_types
 init_type_list          |       |           ^           
+--------------------+   |       +--------+  +--------------+
| MODULE_INIT_BLOCK  |   |                |                 |
+--------------------+   |     +------+   |     +------+    |  +------+
| MODULE_INIT_OPTS   |   +-----+ init |   +-----+ init |    +--+ init |
+--------------------+         +------+         +------+       +------+
| MODULE_INIT_QOM    +-------->+ node +-------->+ node +------>+ node |
+--------------------+         +------+         +------+       +------+
| MODULE_INIT_TRACE  |         | type |         | type |       | type |
+--------------------+         +------+         +------+       +------+
| ...                |
+--------------------+
```

在 `main` 函数中, 调用了`module_call_init(MODULE_INIT_QOM)`, 这个函数执行了 `init_type_list[MODULE_INIT_QOM]` 链表上每一个 `ModuleEntry` 的 `init` 函数
```c
// main.c
int main(int argc, char **argv) {
    // ...
    error_init(argv[0]);
    module_call_init(MODULE_INIT_TRACE);
    qemu_init_cpu_list();
    module_call_init(MODULE_INIT_QOM);
    // ...
}
// util/module.c
void module_call_init(module_init_type type)
{
    ModuleTypeList *l;
    ModuleEntry *e;

    if (modules_init_done[type]) {
        return;
    }

    l = find_type(type);

    QTAILQ_FOREACH(e, l, node) {
        e->init();
    }

    modules_init_done[type] = true;
}
```

这里的QOM对象 `init` 初始化执行 `pci_edu_register_types` 方法, 最终调用核心函数 `type_register_internal(info);`
```c
struct TypeImpl
{
    const char *name;

    size_t class_size;

    size_t instance_size;
    size_t instance_align;

    void (*class_init)(ObjectClass *klass, void *data);
    void (*class_base_init)(ObjectClass *klass, void *data);

    void *class_data;

    void (*instance_init)(Object *obj);
    void (*instance_post_init)(Object *obj);
    void (*instance_finalize)(Object *obj);

    bool abstract;

    const char *parent;
    TypeImpl *parent_type;

    ObjectClass *class;

    int num_interfaces;
    InterfaceImpl interfaces[MAX_INTERFACES];
};
struct TypeInfo
{
    const char *name;
    const char *parent;

    size_t instance_size;
    size_t instance_align;
    void (*instance_init)(Object *obj);
    void (*instance_post_init)(Object *obj);
    void (*instance_finalize)(Object *obj);

    bool abstract;
    size_t class_size;

    void (*class_init)(ObjectClass *klass, void *data);
    void (*class_base_init)(ObjectClass *klass, void *data);
    void *class_data;

    InterfaceInfo *interfaces;
};
static TypeImpl *type_register_internal(const TypeInfo *info)
{
    TypeImpl *ti;
    ti = type_new(info);

    type_table_add(ti);
    return ti;
}
```

### MemoryRegion