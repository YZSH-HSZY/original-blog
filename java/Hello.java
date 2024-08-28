// Hello.java
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