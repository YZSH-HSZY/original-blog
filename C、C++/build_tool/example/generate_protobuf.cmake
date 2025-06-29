include(CMakeParseArguments)

function(add_generate_protobuf_target)
    set(options QUIET)
    set(oneValueArgs NAME PROTO_DIR OUT_DIR)
    set(multiValueArgs)
    cmake_parse_arguments(ARG "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    if(NOT PROTOBUF_PROTOC_EXECUTABLE)
        find_program(PROTOBUF_PROTOC_EXECUTABLE protoc)
    endif()

    if(NOT EXISTS "${PROTOBUF_PROTOC_EXECUTABLE}")
        message(FATAL_ERROR 
            "depend executable protoc not found!")
    endif()

    if(NOT ARG_PROTO_DIR OR NOT IS_DIRECTORY ${ARG_PROTO_DIR})
        message(FATAL_ERROR 
            "add_generate_protobuf_target requires PROTO_DIR <dir> or the dir is not directory")
    endif()
    if(NOT ARG_OUT_DIR)
        message(FATAL_ERROR 
            "add_generate_protobuf_target requires OUT_DIR <dir>")
    endif()

    file(MAKE_DIRECTORY ${ARG_OUT_DIR})

    file(GLOB_RECURSE MSG_PROTOS ${ARG_PROTO_DIR}/*.proto)
    set(MESSAGE_SRC "")
    set(MESSAGE_HDRS "")

    # register the proto files
    foreach(msg ${MSG_PROTOS})
        get_filename_component(FIL_WE ${msg} NAME_WE)

        list(APPEND MESSAGE_SRC "${ARG_OUT_DIR}/${FIL_WE}.pb.cc")
        list(APPEND MESSAGE_HDRS "${ARG_OUT_DIR}/${FIL_WE}.pb.h")

        add_custom_command(
          OUTPUT "${ARG_OUT_DIR}/${FIL_WE}.pb.cc"
                 "${ARG_OUT_DIR}/${FIL_WE}.pb.h"
          COMMAND  ${PROTOBUF_PROTOC_EXECUTABLE}
          ARGS --cpp_out  ${ARG_OUT_DIR}
            -I ${ARG_PROTO_DIR}
            ${msg}
          DEPENDS ${msg}
          COMMENT "Running C++ protocol buffer compiler on ${msg}"
          VERBATIM
        )
    endforeach()
    set_source_files_properties(${MESSAGE_SRC} ${MESSAGE_HDRS} PROPERTIES GENERATED TRUE)

    add_custom_target(generate_proto_message ALL
        DEPENDS ${MESSAGE_SRC} ${MESSAGE_HDRS}
        COMMENT "generate proto message target"
        VERBATIM
        )

endfunction(add_generate_protobuf_target)
