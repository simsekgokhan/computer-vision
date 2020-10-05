cmake_minimum_required(VERSION 2.8)
project( face_detect )

find_package(OpenCV REQUIRED PATHS "/usr/local/Cellar/opencv/4.4.0_2")
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( face_detect main.cpp )
target_link_libraries( face_detect ${OpenCV_LIBS} )