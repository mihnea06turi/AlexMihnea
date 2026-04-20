#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

last_print_time = 0

def callback(msg):
    global last_print_time
    current_time = rospy.get_time()
    
    if current_time - last_print_time >= 0.5:
        fata = msg.ranges[0]
        stanga = msg.ranges[90]
        dreapta = msg.ranges[270]
	
	if fata < 1.0:
		move(pub, 0.0, 1.0, 0)    # viraj stanga
		if dreapta < 1.0:
			move(pub, 0.0, 1.0, 0)
		if stanga < 1.0:
			move(pub , 0.0, -1.0, 0)
	else if fata > 1.0:
		move(pub, 0.0, 0.0, 0.5) #mers in fata
        
        last_print_time = current_time

def listener():
    global pub
    rospy.init_node('perete_detector')
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    rospy.Subscriber("/scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()    



