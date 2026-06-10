#!/usr/bin/env python3
import rospy
import actionlib
from refacere_q3.msg import gardademediuAction, gardademediuFeedback, gardademediuResult
from std_msgs.msg import Empty

def callback_dezinfectare(cerere):
    raport = gardademediuFeedback()
    rezultat_final = gardademediuResult()
    betadina = Empty()
    
    if cerere.dezinfectare == "TAKEOFF":
        pub_carantina.publish(betadina)
        for i in range(5):
            if server_spital.is_preempt_requested():
                server_spital.set_preempted()
                return
            raport.dezinfectat = "take off"
            server_spital.publish_feedback(raport)
            rospy.sleep(1.0)
            
    elif cerere.dezinfectare == "LAND":
        pub_externare.publish(betadina)
        for i in range(5):
            if server_spital.is_preempt_requested():
                server_spital.set_preempted()
                return
            raport.dezinfectat = "landing"
            server_spital.publish_feedback(raport)
            rospy.sleep(1.0)
    
    server_spital.set_succeeded(rezultat_final)

if __name__ == '__main__':
    rospy.init_node('nod_sanitar')
    pub_carantina = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    pub_externare = rospy.Publisher('/drone/land', Empty, queue_size=1)
    server_spital = actionlib.SimpleActionServer("dezinfectant_as", gardademediuAction, callback_dezinfectare, False)
    server_spital.start()
    rospy.spin()
