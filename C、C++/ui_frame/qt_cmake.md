# use qt in cmake

## example

```cmake
cmake_minimum_required(VERSION 3.18)
project(test_qt)
cmake_policy(SET CMP0028 NEW)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
find_package(Qt5 COMPONENTS Core REQUIRED)
# find_package(Qt5Core REQUIRED)  # will find Qt5CoreConfig.cmake file

message(STATUS "Qt5_DIR: ${Qt5_DIR}; Qt5Core_DIR: ${Qt5Core_DIR}")
include_directories(.)
include_directories(${Qt5Core_INCLUDE_DIRS})
include_directories(../..)

set(SOURCES_FILES test.cpp)

if(MSVC)
    add_executable(test_exe ${SOURCES_FILES})
else()
    add_executable(test_exe ${SOURCES_FILES})
endif()

target_link_libraries(test_exe PRIVATE Qt5::Core)
```