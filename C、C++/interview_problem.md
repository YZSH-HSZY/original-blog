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
