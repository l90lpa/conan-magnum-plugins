cmake_minimum_required(VERSION 2.8.12)
project(cmake_wrapper)

include(conanbuildinfo.cmake)
conan_basic_setup()

if(WITH_IMGUI)
  add_library(ImGui::ImGui INTERFACE IMPORTED)
  set_property(TARGET ImGui::ImGui APPEND PROPERTY INTERFACE_LINK_LIBRARIES ${CONAN_LIBS_IMGUI})
  set(ImGui_INCLUDE_DIR ${CONAN_INCLUDE_DIRS_IMGUI})

  add_library(ImGui::Sources INTERFACE IMPORTED)
  set_property(TARGET ImGui::Sources APPEND PROPERTY INTERFACE_LINK_LIBRARIES ImGui::ImGui)
endif()

add_subdirectory("source_subfolder")
