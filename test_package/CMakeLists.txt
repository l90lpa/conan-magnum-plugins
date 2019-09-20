cmake_minimum_required(VERSION 2.8.12)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test-package test_package.cpp)
target_link_libraries(test-package ${CONAN_LIBS})

set_target_properties(test-package 
    PROPERTIES 
    	CXX_STANDARD 17
    	CXX_STANDARD_REQUIRED ON
    	CXX_EXTENSIONS OFF
	)

message(STATUS "CONAN_LIBS: ${CONAN_LIBS}")
      
add_executable(test-assimp-plugin EXCLUDE_FROM_ALL test_assimp_plugin.cpp)
target_link_libraries(test-assimp-plugin ${CONAN_LIBS})      
set_target_properties(test-assimp-plugin
    PROPERTIES 
    	CXX_STANDARD 17
    	CXX_STANDARD_REQUIRED ON
    	CXX_EXTENSIONS OFF
	)

add_executable(test-freetype-plugin EXCLUDE_FROM_ALL test_freetype_plugin.cpp)
target_link_libraries(test-freetype-plugin ${CONAN_LIBS})      
set_target_properties(test-freetype-plugin
    PROPERTIES 
    	CXX_STANDARD 17
    	CXX_STANDARD_REQUIRED ON
    	CXX_EXTENSIONS OFF
	)
      
