cmake_minimum_required(VERSION 3.16)
project(cppoj LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 20)

include_directories(libraries/ac-library)
include_directories(libraries/testlib)

if(MSVC)
    include_directories(utils/bits_stdc++)
    add_compile_options(/Zc:__cplusplus)
    add_definitions(-D_CRT_SECURE_NO_WARNINGS)
endif()

file(GLOB_RECURSE CPP_FILES src/*.cpp)

foreach(CPP_FILE ${CPP_FILES})
    get_filename_component(CPP_FILE_NAME ${CPP_FILE} NAME_WE)
    add_executable(${CPP_FILE_NAME} ${CPP_FILE})
    target_precompile_headers(${CPP_FILE_NAME} PRIVATE <bits/stdc++.h>)
endforeach()

file(TOUCH ${CMAKE_CURRENT_BINARY_DIR}/dummy.cpp)
add_library(dummy ${CMAKE_CURRENT_BINARY_DIR}/dummy.cpp)
