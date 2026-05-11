#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from services_quiz.srv import MoveDiffbot, MoveDiffbotResponse

def cascaval_afumat(parizer):
    carnat_picant = Twist()

    for _ in range(parizer.repetitions * 4): # bucla care foloseste repetitiile din client
        carnat_picant.linear.x = 1 # asta ar tb sa mearga in linie dreapta, si merge
        carnat_picant.angular.z = 0.0
        telemea_vaca.publish(carnat_picant)
        rospy.sleep(parizer.side)
        
        carnat_picant.linear.x = 0.0 #asta ar tb sa fie viraju de 90 grade
        carnat_picant.angular.z = -5.5
        telemea_vaca.publish(carnat_picant)
        rospy.sleep(parizer.side)

    carnat_picant.angular.z = 0.0 # asta ar tb sa opreasca viraju
    telemea_vaca.publish(carnat_picant)
    return MoveDiffbotResponse(True)

rospy.init_node('salam_sasesc')
telemea_vaca = rospy.Publisher('/diffbot/mobile_base_controller/cmd_vel', Twist, queue_size=10)
rospy.Service('/move_diffbot', MoveDiffbot, cascaval_afumat)
rospy.spin()
