### gradle执行顺序

首先 , 执行 settings.gradle 构建脚本 ;
然后 , 查看 系统中 中 是否存在 init.gradle 构建脚本 , 如果有则执行 init.gradle 构建脚本 ; Windows 系统中的 init.gradle 构建脚本 路径 : C:\Users\用户名\.gradle\init.gradle ; ...
最后 , 根据 settings.gradle 脚本中的 子项目 配置 , 选择后续执行子项目的 build.gradle 脚本 ; rootProject.name 用于指定工程根目录 , 在该目录下有一个 build.gradle 构建脚本 , 声明后会自动执行该构建脚本 ; ...

### gradle每次构建均下载maven-metadata.xml文件

- 问题：在android项目中，如果依赖的jar包版本不确定（即是一个范围），那么每个构建时均会下载maven-metadata.xml得到jar包可选版本号。
> 解决方案：1. 更改形如`compile 'com.github.rosjava.android_remocons:common_tools:[0.3,0.4)'`的版本范围为指定版本号
> 2. 如果在本地缓存中已经存在指定范围内的jar包，可以使用gradle离线构建


### gradle不同版本选项更改

#### 指定 maven url 的http安全问题
boolean allowInsecureProtocol
Specifies whether it is acceptable to communicate with a repository over an insecure HTTP connection.
指定是否可接受通过不安全的 HTTP 连接与存储库进行通信。

For security purposes this intentionally requires a user to opt-in to using insecure protocols on case by case basis.
出于安全考虑，这有意要求用户根据具体情况选择使用不安全的协议。

Gradle intentionally does not offer a global system/gradle property that allows a universal disable of this check.
Gradle 特意不提供允许通用禁用此检查的全局系统/gradle 属性。

