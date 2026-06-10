cmake_minimum_required(VERSION 3.0.2)
project(refacere_q3)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  message_generation
  rospy
  std_msgs
)

add_action_files(
  FILES
  gardademediu.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS actionlib actionlib_msgs rospy std_msgs message_runtime
)

#am lasat doar dezinfectantul... aaa... doar ceea ce folosesc in acest fiser, la fel ca la testul 2, ca sa nu ma pierd prin fisier sau sa nu uit un comentariu inainte de o )
