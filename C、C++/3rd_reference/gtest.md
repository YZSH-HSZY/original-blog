# gtest

全称 GoogleTest 是 Google 推出的 C++测试和模拟框架

## 测试宏

### TEST
```c
TEST(TestSuiteName, TestName) {
  ... statements ...
}
```
单个测试套件 TestSuiteName 中定义名为 TestName 的测试

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