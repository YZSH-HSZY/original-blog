# gtest

全称 GoogleTest 是 Google 推出的 C++测试和模拟框架

> [gtest官方文档](https://google.github.io/googletest/)

## 术语

- `Assertions`: GoogleTest 断言是类似于函数调用的宏.通过对类或函数的行为做出断言来测试类或函数. 失败时,会打印断言的源文件和行号位置, 可以提供一个自定义的失败消息(使用 `<< message` 来提供)
> `ASSERT_*`在失败时会生成致命故障，并**中止当前函数**; `EXPECT_*` 生成非致命故障，不会中止当前函数
- `Test Fixtures`: 测试夹具, 使用相同的数据配置进行多项测试

## USAGE

### TEST
```c
TEST(TestSuiteName, TestName) {
  ... statements ...
}
```
单个测试套件 TestSuiteName 中定义名为 TestName 的测试
> **注意** 两个名称都必须是有效的 C++标识符, 并且不应包含任何下划线`_`

### Test Fixtures

创建一个测试夹具的方法如:
1. 编写一个继承 `testing::Test` 的类,数据成员从 `protected` 开始

```cpp
class QueueTest : public testing::Test {
 protected:
  QueueTest() {
     // q0_ remains empty
     q1_.Enqueue(1);
     q2_.Enqueue(2);
     q2_.Enqueue(3);
  }

  // ~QueueTest() override = default;

  Queue<int> q0_;
  Queue<int> q1_;
  Queue<int> q2_;
};
```

```cpp
TEST_F(QueueTest, IsEmptyInitially) {
  EXPECT_EQ(q0_.size(), 0);
}
```

> 第一个参数必须是测试夹具类的名称(此宏不存在测试套件名称)
> 使用 `TEST_F` 前必须先定义测试夹具类, 否则会得到编译错误`virtual outside class declaration`

实际运行时, GoogleTest 将在运行时创建一个新的测试夹具并通过 `SetUp()` 初始化, 通过 `TearDown()` 清理, 然后删除测试夹具, GoogleTest 不会为多个测试重用同一个测试夹具

## Example

### 继承gtest到ctest中

```sh
find_package(GTest REQUIRED)
enable_testing()

add_executable(
  hello_test
  hello_test.cc
)
target_link_libraries(
  hello_test
  GTest::gtest_main
)

include(GoogleTest)
# 使用gtest_discover_tests替代add_test添加到Testfile中
gtest_discover_tests(hello_test)
```