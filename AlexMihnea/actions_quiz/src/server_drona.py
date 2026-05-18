#!/usr/bin/env python3
import rospy
import actionlib
from actions_quiz.msg import MiciAction, MiciFeedback, MiciResult

class CiorbaDeBurta(object):
    _salata_boeuf = MiciFeedback()
    _torta_diplomat = MiciResult()

    def __init__(self):
        self._sarmale = actionlib.SimpleActionServer("mancare_gatita", MiciAction, self.papanasi_callback, False)
        self._sarmale.start()
        
    def papanasi_callback(self, desert):
        cozonac = rospy.Rate(1)
        
        foame = int(desert.distanta_pana_la_gratar)
        for pofta in range(foame):
            self._salata_boeuf.cumetri = float(pofta)
            self._sarmale.publish_feedback(self._salata_boeuf)
            cozonac.sleep()
            
        self._torta_diplomat.mici_cu_mustar = True
        self._sarmale.set_succeeded(self._torta_diplomat)

if __name__ == '__main__':
    rospy.init_node('nod_pregatar')
    CiorbaDeBurta()
    rospy.spin()