##### spring boot test

spring 项目内部的框架细节和相关的依赖配置较多，如果使用一般的测试需要进行的环境搭建较为繁杂，而 spring-boot-test 可以简化测试环境搭建流程。

1. spring-boot-test 即对 spring 项目进行测试。需要添加依赖

```
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <version>2.3.7.RELEASE</version>
        <scope>test</scope>
    </dependency>
```

范围 scope 中指定测试 test 有效，即只在测试编译和测试运行时会导入该库

2. 使用@SpringBootTest 注解会自动将 spring 项目的上下文准备好以应用于测试中，对传统 spring 项目的 repository，service，controller 层均有相应的内部工具类进行测试。

3. spring-boot-starter-test 包含 junit 和 assertj 和 mockito 等测试工具，对于自动装载的 bean 可以通过@MockBean 或@SpyBean 来模拟或打桩获取，对 MVC 模式的 http 请求提供了 MockMvc 类进行模拟及 MockMultipartFile 模拟文件

```
@ExtendWith(SpringExtension.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
public class ServiceTest {
    //TODO
}
```

> 在上述代码中，演示了一个 SpringBootTest 测试类，其中
> 1.@ExtendWith(SpringExtension.class)告诉 junit 测试使用 spring 相关配置。
> 2.webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT 指使用随机端口启动项目（如果你使用 websocket 工具，可能会出现端口冲突导致 spring 项目启动失败），可以使用@LocalServerPort 注解获取随机端口。
> 3.@AutoConfigureMockMvc 注解可以自动化配置注入的 MockMvc 对象。
> 以下是一个上传文件的测试示例：

```
    //@Transactional注解在测试数据库是对操作进行回滚处理
    @Test
    @Transactional
    @DisplayName("图书上传测试")
    public void bookUploadTest() {
        //模拟上传文件,第一个参数表示请求名，与规定的请求名保持一致，第二个参数为原始文件名
        MockMultipartFile file = new MockMultipartFile(
                "file", "sample2.txt",
                "text/plain", "This is a file context at controller test".getBytes(StandardCharsets.UTF_8));
        //构建文件上传请求.multipart("/common/upload")
        MockMultipartHttpServletRequestBuilder multipart = MockMvcRequestBuilders.multipart("/common/upload");
        try {
            MvcResult result = mockMvc.perform(multipart
                    .file(file)
                    .headers(InitHandleTest.headers))
                    .andExpect(MockMvcResultMatchers.status().isOk())
                    .andDo(MockMvcResultHandlers.print())
                    .andReturn();
            JSONObject json = JSONObject.parseObject(result.getResponse().getContentAsString());
            //验证返回响应的body不为空,并且包含字段fileName
            org.assertj.core.api.Assertions.assertThat(json).isNotNull();
            org.assertj.core.api.Assertions.assertThat(json.getString("fileName")).isNotNull();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
```

4. 在 spring boot test 项目中，如果需要获取项目自动配置的 Bean 对象，可以通过 spring 提供的 ApplicationContext 应用上下文来获取，需要对应 Bean 类型的 class 对象作为参数。示例代码如下：

```
    @Autowired
    private ApplicationContext applicationContext;

    @ParameterizedTest
    @CsvFileSource(resources = "/repository/select_list_test.csv")
    @DisplayName("测试读取mysql数据库的查询操作")
    public void selectTest(String mapperClassName, String entityClassName) {
        try {
            //根据类全名获取mapper接口的class对象
            Class<?> needClass = Class.forName(mapperClassName);
            //根据类全名获取mapper接口中select方法的参数类型的class对象
            Class<?> needClassArg = Class.forName(entityClassName);
            List<Method> methods = Arrays.asList(needClass.getDeclaredMethods());
            String pattern = "^select.*List$";
            for (int i = 0; i < methods.size(); i++) {
                if(Pattern.matches(pattern, methods.get(i).getName())){
                    System.out.println(methods.size());
                    methods.get(i).invoke(applicationContext.getBean(needClass), needClassArg.newInstance());
                }
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        } catch (InstantiationException e) {
            e.printStackTrace();
        }
    }
```
