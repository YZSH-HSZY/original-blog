## 多态实现方式

1. 静态多态（重载/模板/重写）

是在编译的时候，就确定调用函数的类型。

2. 动态多态（重写:虚函数实现）

在运行的时候，才确定调用的是哪个函数，动态绑定。运行基类指针指向派生类的对象，并调用派生类的函数。

虚函数实现原理：虚函数表和虚函数指针。

**注意** 普通重写和虚函数重写编译器所采取的实现多态方式不同，普通重写是静态多态，在编译期间确定，虚函数重写实现的多态，会为对象维护一个虚函数表，在虚函数表中确认需要调用的函数位置。可以使用-S选项查看生成的汇编码确认差别，如：
```C++
#include <iostream>
using namespace std;
class A{
public:
    void test_func();  // 1
    // virtual void test_func();  // 2
};
class B: A
{
public:
    void test_func();
};
void A::test_func(){
    cout << "A test_func" << endl;
}
void B::test_func(){
    cout << "B test_func" << endl;
}
int main(){
    cout << "Hello World" << endl;
    B* p = new B();
    p->test_func();
    ((A*)p)->test_func();
    delete (B*)p;
    return 0;
}

> g++ -S test_overwrite.cpp 
output:
1. 普通重写
	call	_ZN1B9test_funcEv
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	_ZN1A9test_funcEv
	movq	-8(%rbp), %rax
	testq	%rax, %rax
	je	.L4
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZdlPvm@PLT
2. 虚函数重写
	call	*%rdx
	movq	-24(%rbp), %rax
	movq	(%rax), %rax
	movq	(%rax), %rdx
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	*%rdx
	movq	-24(%rbp), %rax
	testq	%rax, %rax
	je	.L6
	movl	$8, %esi
	movq	%rax, %rdi
	call	_ZdlPvm@PLT
```
可以看到两个call指令的调用区别

## 虚函数和纯虚函数

## 类型转换

## 智能指针

## RVO和移动语义

> 我关于RVO和移动语义的理解:
> 移动语义用于Pimpl实现的容器和资源分离，在移动构造中会提供类似指针的操作转义资源的所有权，而返回值优化是编译器做的，可以减少内部对象(即出栈的一次临时对象拷贝)

**总结**
- 移动语义: 语言级别的资源所有权转移机制
	* 用于 Pimpl、智能指针、容器等
	* 类似指针操作的成本
	* 程序员显式控制
- RVO/NRVO: 编译器级别的优化技术
	* 消除函数返回时的临时对象
	* 减少一次拷贝/移动操作
	* 编译器自动进行，无需程序员干预

**关系** 移动语义是 RVO 失效时的备选方案, RVO 比移动语义更高效（零成本）
> 现代 C++ 中两者配合提供高效的返回值处理. 移动语义处理资源所有权的显式转移，而 RVO 是编译器消除临时对象的隐式优化

## vector相关

### resize/reserve的区别

| 特性             | `reserve(size_t n)`     | `resize(size_t n)` |
|-----------------|--------------------------|-------------------|
| **主要目的**     | 预分配内存，避免扩容开销  | 改变 vector 的实际大小 |
| **容量变化**     | `capacity() >= n`       | `capacity()` 可能增加（如果需要） |
| **大小变化**     | `size()` 不变           | `size()` 变为 `n` |
| **元素变化**     | 不创建/销毁元素          | 创建新元素或删除多余元素 |
| **访问新增元素** | 未定义行为（不能访问）    | 可以安全访问 |
| **性能影响**     | 减少后续插入的开销        | 立即构造/析构元素 |
| **迭代器有效性** | 可能失效（如果重新分配）   | 可能失效（如果重新分配） |
| **典型用途**     | 性能优化                 | 初始化或调整容器大小 |

**注意** `reserve` 不保证精准容量

## 堆栈相关

### 如何确保生成一个堆对象/栈对象

**栈对象生成**
- 私有化 `new`/`new []` 限制堆对象创建
```cpp
void* operator new(size_t size) = delete;
void operator delete(void* ptr) = delete;
void* operator new[](size_t size) = delete;
void operator delete[](void* ptr) = delete;
```
- 使用私有构造和静态工厂方法
- 结合 placement new 限制