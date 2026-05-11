cmake_minimum_required(VERSION 3.0.2)
project(services_quiz)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  message_generation
)

add_service_files(FILES MoveDiffbot.srv)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(CATKIN_DEPENDS rospy geometry_msgs message_runtime)

include_directories(${catkin_INCLUDE_DIRS})

#am sters tot din cmakelist si package.xml, pt ca ma incurc in atatea linii de cod, prefer sa am curat totul una sub alta, ca in caz ca uit ceva sa am de unde sa le iau, sa nu uit un # inainte de o paranteza, si lista poate continua. prefer sa lucrez in 30 de linii decat in 30.
