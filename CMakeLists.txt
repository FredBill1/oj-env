cmake_minimum_required(VERSION 3.15)
project(cppoj LANGUAGES C CXX)

file(GLOB_RECURSE CPP_FILES src/*.cpp)
set(CMAKE_CXX_STANDARD 20)

foreach(CPP_FILE ${CPP_FILES})
    get_filename_component(CPP_FILE_NAME ${CPP_FILE} NAME_WE)
    add_executable(${CPP_FILE_NAME} ${CPP_FILE})
    target_include_directories(${CPP_FILE_NAME} PRIVATE include)
endforeach()
