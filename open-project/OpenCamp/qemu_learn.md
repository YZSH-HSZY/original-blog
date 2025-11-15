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
// bsd-user/main.c(User Model Simulation Entry Point)
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

**注意** `TypeImpl` 的数据基本上都是从 `TypeInfo` 复制过来的, 表示的是一个类型的基本信息。类似于 C++ 中，class 关键字定义的一个类型

#### 类型的初始化

在 C++ 等面向对象的编程语言中, 当程序声明一个类型的时候, 就已经知道了其类型的信息, 比如它的对象大小。 但如果使用 C 语言来实现面向对象的这些特性, 就需要做特殊的处理, 对类进行单独的初始化。

类的初始化使用 `type_initialize(TypeImpl *ti)` 完成的

```c
// qom/object.c
static void type_initialize(TypeImpl *ti)
{
    TypeImpl *parent;

    if (ti->class) {
        return;
    }

    // 1. 设置相关 filed
    ti->class_size = type_class_get_size(ti);
    ti->instance_size = type_object_get_size(ti);
    ti->instance_align = type_object_get_align(ti);
    /* Any type with zero instance_size is implicitly abstract.
     * This means interface types are all abstract.
     */
    if (ti->instance_size == 0) {
        ti->abstract = true;
    }
    if (type_is_ancestor(ti, type_interface)) {
        assert(ti->instance_size == 0);
        assert(ti->abstract);
        assert(!ti->instance_init);
        assert(!ti->instance_post_init);
        assert(!ti->instance_finalize);
        assert(!ti->num_interfaces);
    }
    ti->class = g_malloc0(ti->class_size);

    // 2. 初始化所有父类类型
    parent = type_get_parent(ti);
    if (parent) {
        type_initialize(parent);
        GSList *e;
        int i;

        g_assert(parent->class_size <= ti->class_size);
        g_assert(parent->instance_size <= ti->instance_size);
        memcpy(ti->class, parent->class, parent->class_size);
        ti->class->interfaces = NULL;

        for (e = parent->class->interfaces; e; e = e->next) {
            InterfaceClass *iface = e->data;
            ObjectClass *klass = OBJECT_CLASS(iface);

            type_initialize_interface(ti, iface->interface_type, klass->type);
        }

        for (i = 0; i < ti->num_interfaces; i++) {
            TypeImpl *t = type_get_by_name_noload(ti->interfaces[i].typename);
            if (!t) {
                error_report("missing interface '%s' for object '%s'",
                             ti->interfaces[i].typename, parent->name);
                abort();
            }
            for (e = ti->class->interfaces; e; e = e->next) {
                TypeImpl *target_type = OBJECT_CLASS(e->data)->type;

                if (type_is_ancestor(target_type, t)) {
                    break;
                }
            }

            if (e) {
                continue;
            }

            type_initialize_interface(ti, t, t);
        }
    }

    ti->class->properties = g_hash_table_new_full(g_str_hash, g_str_equal, NULL,
                                                  object_property_free);

    ti->class->type = ti;

    // 3. 依次调用所有父类的初始化函数（与 C++ 类似）
    while (parent) {
        if (parent->class_base_init) {
            parent->class_base_init(ti->class, ti->class_data);
        }
        parent = type_get_parent(parent);
    }

    if (ti->class_init) {
        ti->class_init(ti->class, ti->class_data);
    }
}
```

**注意** `type_initialize`的调用时机是在需要时才会调用

#### 类型的层次结构

在 `type_initialize` 中, 类型初始化的时候也会初始化父类型。QOM 通过这种层次结构实现类似 C++ 中的继承概念
以 edu 设备为例:
```c
// hw/misc/edu.c
    static const TypeInfo edu_info = {
        .name          = TYPE_PCI_EDU_DEVICE,
        .parent        = TYPE_PCI_DEVICE,
        ...
    };
// hw/pci/pci.c
static const TypeInfo pci_device_type_info = {
    .name = TYPE_PCI_DEVICE,
    .parent = TYPE_DEVICE,
    ...
};
// hw/core/qdev.c
static const TypeInfo device_type_info = {
    .name = TYPE_DEVICE,
    .parent = TYPE_OBJECT,
    .class_init = device_class_init,
    .abstract = true,
    ...
};
// qom/object.c
static const TypeInfo object_info = {
    .name = TYPE_OBJECT,
    .instance_size = sizeof(Object),
    .class_init = object_class_init,
    .abstract = true,
};
```

edu类型的层次结构为:
`TYPE_PCI_EDU_DEVICE -> TYPE_PCI_DEVICE -> TYPE_DEVICE -> TYPE_OBJECT`

> 数据结构上类型的层次结构

类型初始化函数 type_initialize 中会调用 `ti->class = g_malloc0(ti->class_size);` 分配类型的 class 结构，这个结构实际上代表了类型的信息。类似于 C++ 定义的一个类。

**注意** class_size 是 TypeImpl 的一个字段，如果这个类型没有指明它，则会使用父类的 class_size 进行初始化, 参
```c
// qom/object.c
static void type_initialize(TypeImpl *ti)
{
    ...
    ti->class_size = type_class_get_size(ti);
    ...
}

static size_t type_class_get_size(TypeImpl *ti)
{
    if (ti->class_size) {
        return ti->class_size;
    }

    if (type_has_parent(ti)) {
        return type_class_get_size(type_get_parent(ti));
    }

    return sizeof(ObjectClass);
}
```

**注意** 这里的 edu 设备类型本身没有定义 `class_size`, 因此他的 `class_size` 为其父类的 `class_size`, 这里指 `TYPE_PCI_DEVICE` 设备的 `class_size`, 如下:
```c
// hw/pci/pci.c
static const TypeInfo pci_device_type_info = {
    .name = TYPE_PCI_DEVICE,
    .parent = TYPE_DEVICE,
    .instance_size = sizeof(PCIDevice),
    .abstract = true,
    .class_size = sizeof(PCIDeviceClass),
    .class_init = pci_device_class_init,
    .class_base_init = pci_device_class_base_init,
};
```

#### 对象的构造与初始化

对象的构造流程，主要是通过 object_new 函数来实现，调用链如下:
`object_new() -> object_new_with_type() -> object_initialize_with_type() -> object_init_with_type()`

> `object_new_with_type`代码如下, 会先初始化父类
```c
// qom/object.c
static void object_init_with_type(Object *obj, TypeImpl *ti)
{
    if (type_has_parent(ti)) {
        object_init_with_type(obj, type_get_parent(ti));
    }

    if (ti->instance_init) {
        ti->instance_init(obj);
    }
}
```
> 类型和对象之间是通过 Object 的 class 域联系在一起: `obj->class=type->class`

> 把 QOM 的对象构造分成 3 部分

1. 类型的构造，通过 TypeInfo 构造一个 TypeImpl 的哈希表，在 main 之前完成
2. 类型的初始化，在 main 中进行，类型的构造和初始化是全局性的，编译进去的 QOM 对象都会调用
3. 类对象的构造，构造具体的实例对象，只会对指定的设备，创建对象

> 上述步骤之后, 构造出了对象并完成了对象的内存初始化, 但还缺少数据部分的填充, 此时edu设备还是不可用的, 对设备而言, 还需要设置它的 realized 属性为 true 才行, 调用链如下所示:
`qemu-6.0.0: softmmu/main.c:main --> softmmu/vl.c:qemu_init --> softmmu/vl.c:qmp_x_exit_preconfig --> softmmu/vl.c:qemu_create_cli_devices --> softmmu/vl.c:device_init_func --> softmmu/qdev-monitor.c:qdev_device_add --> hw/core/qdev.c:qdev_realize`

> `qdev_realize` 设置 对象的 `realized` 为 `true` :
```c
bool qdev_realize(DeviceState *dev, BusState *bus, Error **errp)
{
    assert(!dev->realized && !dev->parent_bus);

    if (bus) {
        if (!qdev_set_parent_bus(dev, bus, errp)) {
            return false;
        }
    } else {
        assert(!DEVICE_GET_CLASS(dev)->bus_type);
    }
    return object_property_set_bool(OBJECT(dev), "realized", true, errp);
}
```

#### 对象的属性

> QOM 实现了类似 C++ 的基于类的多态, 一个对象按照继承体系进行互相转换, 如: `Object <-- DeviceState <-- PCIDevice`等. 

**注意** QOM中继承时指针的转换依赖于对象的内存布局, 如 `Object <-- DeviceState <-- PCIDevice` 继承体系中, 如:
```c
struct Object
{
    /* private: */
    ObjectClass *class;
    ...
};
struct DeviceState {
    /*< private >*/
    Object parent_obj;
    /*< public >*/
    ...
};
struct PCIDevice {
    DeviceState qdev;
    ...
};
// 可以看到在这种单继承体系中, 第一个成员即为父对象的数据成员
```


> 在 QOM 中为了便于管理对象, 还给每种类型已经对象增加了属性. 其中:
- 类属性存在于 `ObjectClass` 的 `properties` 域中，在 `type_initialize` 中构造
- 对象属性存在于 `Object` 的 `properties` 域中，这个域在 `object_initialize_with_type` 中构造

**注意** `properties` 为一个哈希表, 存在属性名字到 `ObjectProperty` 的映射

```c
// qom/object.h
struct ObjectProperty
{
    char *name;
    char *type;
    char *description;
    ObjectPropertyAccessor *get;
    ObjectPropertyAccessor *set;
    ObjectPropertyResolve *resolve;
    ObjectPropertyRelease *release;
    ObjectPropertyInit *init;
    void *opaque;
    QObject *defval;
};
// 每一种具体的属性, 会有一个结构体来描述它
// qom/object.c
typedef struct {
    union {
        Object **targetp;
        Object *target; /* if OBJ_PROP_LINK_DIRECT, when holding the pointer  */
        ptrdiff_t offset; /* if OBJ_PROP_LINK_CLASS */
    };
    void (*check)(const Object *, const char *, Object *, Error **);
    ObjectPropertyLinkFlags flags;
} LinkProperty;

typedef struct StringProperty
{
    char *(*get)(Object *, Error **);
    void (*set)(Object *, const char *, Error **);
} StringProperty;
```

> 属性的添加: 分为类属性的添加和对象属性的添加, 如对象属性添加是通过 `object_property_add` 接口完成的, 其内存布局大概如下:
```
+----------------+                                                                 
| ...            |                                                                 
+----------------+                                                                 
|   properties   +-------------+-------------------------------------------------  
+----------------+             |                                                   
| ...            |         +---+----+                                              
|                |         | name   |                                              
|                |         +--------+                                              
|                |         | type   |                                              
+----------------+         +--------+                                              
Object                     | set    +---> property_set_bool                        
                           +--------+                                              
                           | get    +---> property_get_bool                        
                           +--------+                                              
                           | opaque +---------> +-------+                          
                           +--------+           |  get  +--> memfd_backend_get_seal
                          ObjectProperty        +-------+                          
                                                |  set  +--> memfd_backend_set_seal
                                                +-------+                          
                                               BoolProperty       
```

> 对象属性中两种特殊属性
- child 属性: 表对象之间的从属关系, 通过 ` object_property_add_child` 添加
- link 属性: 表一种连接关系, 代表一个设备引用了另一个设备, 通过 `object_property_add_link` 添加

> 参设备对象添加链接属性 `gpio_itq` 示例:
```c
void qdev_init_gpio_out_named(DeviceState *dev, qemu_irq *pins,
                              const char *name, int n)
{
    int i;
    NamedGPIOList *gpio_list = qdev_get_named_gpio_list(dev, name);

    assert(gpio_list->num_in == 0 || !name);

    if (!name) {
        name = "unnamed-gpio-out";
    }
    memset(pins, 0, sizeof(*pins) * n);
    for (i = 0; i < n; ++i) {
        gchar *propname = g_strdup_printf("%s[%u]", name,
                                          gpio_list->num_out + i);

        object_property_add_link(OBJECT(dev), propname, TYPE_IRQ, // link 来连接两个 qdev
                                 (Object **)&pins[i],
                                 object_property_allow_set_link,
                                 OBJ_PROP_LINK_STRONG);
        g_free(propname);
    }
    gpio_list->num_out += n;
}
```


#### 总结

> 上述描述中, 已经较为完整的说明了QEMU如何添加一个自定义设备, 现在总结一个设备类的定义如下:

1. 首先每个类型指定一个 TypeInfo 注册到系统中；
2. 接着系统运行初始化的时候会把 TypeInfo 转变成 TypeImpl 放到一个哈希表中
3. 系统会对这个哈希表中的每个类型进行初始化；
4. 接下来根据 QEMU 命令行参数，创建对应的实例对象。

### 地址空间抽象

从 CPU 的角度来说，一切访存行为都是对地址进行操作的(load/store)，CPU 并不关心这个地址背后对应的是什么设备，只要能读写到正确结果即可. QEMU 提供了一套内存模拟的机制来实现cpu对设备的访问

> 为了模拟内存/外设的行为, QEMU 至少要实现以下机制:
1. 基本的地址空间管理，能够根据 CPU 投递过来的地址，区分是什么设备
2. 实现地址的离散映射，有些外设的地址不一定是连续的
3. 实现地址的重映射，比如 MCS-51 的 RAM、XRAM 都是从 0 地址开始的

> QEMU 提供了两个概念 `address-space` 和 `memory-region`（简称为 mr），前者用于描述整个地址空间的映射关系（不同部件看到的地址空间可能不同），后者用于描述地址空间中某个地址范围内的映射规则

### MemoryRegion