
# 非window平台链接anl库
target_link_libraries(${PROJECT_NAME} $<$<NOT:$<PLATFORM_ID:Windows>>:anl>)

# window平台链接ws2_32
target_link_libraries(${PROJECT_NAME} $<$<PLATFORM_ID:Windows>:ws2_32>)


if(TEST_OPEN)

endif()