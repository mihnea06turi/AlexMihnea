#! /usr/bin/env python

import rospy                                          
from std_msgs.msg import Int32 

def callback(msg):                            	# Define a function called 'callback' that receives a parameter named 'msg'
    print (msg.data)     
    if (msg.data % 3 == 0):
        print('Se divide cu 3')                       	# Print the value 'data' inside the 'msg' parameter

rospy.init_node('divizibil3')                   	# Initiate a Node called 'topic_subscriber'
sub = rospy.Subscriber('/div3', Int32, callback)   	# Create a Subscriber object that will listen to the /counter
                                                      			# topic and will call the 'callback' function each time it reads
                                                      			# something from the topic
rospy.spin()                                          			# Create a loop that will keep the program in execution
