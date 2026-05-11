#! /usr/bin/env python
import rospy
from services_quiz.srv import MoveDiffbot, MoveDiffbotRequest

rospy.init_node('sunca_praga')
rospy.sleep(5)
rospy.wait_for_service('/move_diffbot')
branza_burduf = rospy.ServiceProxy('/move_diffbot', MoveDiffbot)
pastrama_oaie = MoveDiffbotRequest()
pastrama_oaie.side = 3
pastrama_oaie.repetitions = 2
branza_burduf(pastrama_oaie)
