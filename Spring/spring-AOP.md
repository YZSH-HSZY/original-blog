### AOP(面向切面编程)

1. 在 spring 中我们可以使用 AOP 来进行日志的记载和其他的一些通知操作，主要时对已有的方法进行增强。
2. aspectj 是目前比较流行的 AOP 框架，可以在 pom.xml 中导入依赖

```
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-aop</artifactId>
    </dependency>
```

spring-AOP 中提供 aspectj 支持

### aspectj 的使用


示例如下：

```
/**
 * 测试的切面配置
 */
@Aspect
@Component
public class SysControllerAspect {

    /** controller层list方法切点 */
    @Pointcut("execution(public * com.ruoyi..*.list(..))")
    public void getList() {};

    @Before("getList()")
    public void doBefore(JoinPoint joinPoint) {
        MethodSignature signature = (MethodSignature) joinPoint.getSignature();
        Type type = signature.getMethod().getGenericParameterTypes()[0];

        System.out.println("controller层list 前置通知");
    }

    @AfterReturning(pointcut = "getList()", returning = "result")
    public void doAfter(JoinPoint joinPoint, Object result) {
        System.out.println("controller层list 后置通知");
        // 为所有list请求，根据返回类型断言请求成功
        if(result instanceof TableDataInfo) {
            Assertions.assertThat(((TableDataInfo) result).getCode()).isEqualTo(200);
        }
        if(result instanceof AjaxResult) {
            Assertions.assertThat(((AjaxResult) result).get(AjaxResult.CODE_TAG)).isEqualTo(200);
        }
    }
}
```

> 1.@Aspect 注解表示该类是一个切面类，@Component 注解表示将该切面类交给 spring 自动配置使用。 2.在切点定义@Pointcut 中'\*'表示同一层级下任意字符串，第一个'..'两个点符匹配字符串可越层级，即可递归匹配当前目录即子目录。后一个'..'两个点符匹配方法任意参数。
