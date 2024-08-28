### JNI

JNI 全名（Java Native Interface，Java 原生接口）是一种编程框架，使得 Java 虚拟机中的 Java 程序可以调用==本地应用/或库，也可以被其他程序调用。==

> 有些事情 Java 无法处理时，JNI 允许程序员用其他编程语言来解决，例如，Java 标准库不支持的平台相关功能或者程序库。也可用于改造已存在的用其它语言写的程序，供 Java 程序调用。许多基于 JNI 的标准库提供了很多功能给程序员使用，例如文件 I/O、音频相关的功能。当然，也有各种高性能的程序，以及平台相关的 API 实现，允许所有 Java 应用程序安全并且平台独立地使用这些功能。

**什么时候使用 JNI？**

1. 追求性能，对 Java 虚拟机进行扩展，需要使用 Native 的实现。
2. 已经存在的功能，借助 JNI 协议，不需要重新的 Java 实现。
3. Java 的.class 文件安全性较差，增加安全性，将重要的逻辑在 Native 代码中实现。

**JNI 使用步骤**

1. 编写 JNI 的 java 调用代码，即声明需要调用本地已实现功能的 java 函数
2. 编译.java 文件生成.class 文件，使用 javah 工具生成 c/c++的.h 头文件
3. 实现对应 c/c++源代码，在需要实现的函数体中调用已存在的功能函数完成需要的功能。
4. 编译生成库文件，放到 java 项目的 resource 文件夹或自己指定文件夹下，也可直接放到同一目录下，在 java 代码中调用即可
   示例：

```
编写// Hello.java
public class Hello {
    static {
        /**
         * System.loadLibrary()表明需要加载动态库hello
         * 在不同的系统平台上对应不同的名字
         * 在Windows平台上查找的是hello.dll
         * 在Linux平台上查找的是libhello.so
         * 而在MacOS平台上查找的是libhello.dylib
         */
        System.loadLibrary("hello");
    }

    public native void sayHello();

    public static void main(String[] args) {
        new Hello().sayHello();
    }
}
//生成头文件Hello.h,创建C/C++链接库项目,编写源代码

/* Replace "dll.h" with the name of your header */
#include "dll.h"
#include <windows.h>
//#include "jni_md.h"
#include "JNI.h"
JNIEXPORT void JNICALL Java_Hello_sayHello(JNIEnv * s, jobject s2){
  	printf("Hello JNI!\n");
}
// 我这里忘记了导入头文件，因为比较简单还没出错。自己写的时候记得导入
//问题：
1.JNI.h是外部导入的.h文件，如果对应的库文件目录已添加，仍提示未找到，可以使用双引号包含
2.如果使用的IDE报jni_md.h未找到错误，可以自定义头文件统一包含
3.报参数省略错误可以添加对应参数名
//结果如下：
PS E:\git\blog\java> java Hello
Picked up JAVA_TOOL_OPTIONS: -Dfile.encoding=UTF-8
Hello JNI!
```

### JNA

JNA 全名(java native access)，是一个建立在经典的JNI技术之上的Java开源框架。
JNA 解决了 JNI 中最麻烦的数据类型映射, 可以让我们进行高效的开发, 不用再去写各种的转换接口.

==具有以下好处：==

1. 你不需要通过 javah 生成头文件, 不需要给它写实现
2. 不需要在 windows/linux 环境各自编译成 .dll/.so 来调用真正的函数
3. 只需要声明一个接口, 其他的事情让 JNA 做好就行

**如何使用？**
你可以在pom.xml中添加如下依赖：
```
<dependency>
    <groupId>net.java.dev.jna</groupId>
    <artifactId>jna</artifactId>
    <version>5.3.1</version>
</dependency>
```