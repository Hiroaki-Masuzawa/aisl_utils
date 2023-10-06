cmake_minimum_required(VERSION 2.8.3)
project(instance_segmentation_srvs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  std_srvs
  sensor_msgs
  deep_learning_msgs
  message_generation
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  GetInstanceSegmentation.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  sensor_msgs
  deep_learning_msgs
  std_srvs  # Or other packages containing msgs
)

catkin_package(CATKIN_DEPENDS message_runtime)
