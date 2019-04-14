#!/usr/bin/env python

import rospy
from race.msg import drive_values
from race.msg import drive_param
from std_msgs.msg import Bool


"""
What you should do:
 1. Subscribe to the keyboard messages (If you use the default keyboard.py, you must subcribe to "drive_paramters" which is publishing messages of "drive_param")
 2. Map the incoming values to the needed PWM values
 3. Publish the calculated PWM values on topic "drive_pwm" using custom message drive_values
"""

class Talker():
    def __init__(self):
        rospy.init_node('Talker', anonymous=False)
	rospy.on_shutdown(self.shutdown)
        self.vel = 0
	self.ang = 0
	self.pwm_drive = 0
	self.pwm_angle = 0
	self.rate = rospy.Rate(100)
        self.sub = rospy.Subscriber("drive_parameters", drive_param, self.callback)
        self.pub = rospy.Publisher("drive_pwm", drive_values, queue_size=10)
	rospy.loginfo(" Press CTRL+C to stop driving.")

    def convert_to_pwm(self):
        temp_drive = int(round(9831 + ((3277/100)*self.vel)))
        temp_angle = int(round(9831 + ((3277/100)*self.ang)))
        if(temp_drive > 6554 and temp_drive < 13108):
		self.pwm_drive = temp_drive
        if(temp_angle > 6554 and temp_angle < 13108):
		self.pwm_angle = temp_angle
	
    def talk(self):
	while not rospy.is_shutdown():
	    new_drive_values = drive_values()
            self.convert_to_pwm()
	    new_drive_values.pwm_drive = self.pwm_drive
	    new_drive_values.pwm_angle = self.pwm_angle
	    self.pub.publish(new_drive_values)
	    self.rate.sleep()
    def shutdown(self):
		rospy.loginfo("Stopping the car")
		new_drive_values = drive_values()
		new_drive_values.pwm_drive = 9831
		new_drive_values.pwm_angle = 9831
		self.pub.publish(new_drive_values)
		rospy.sleep(1)

    def callback(self, data):
		self.vel = data.velocity
		self.ang = data.angle 
		print "Velocity: ", self.vel, " Angle: ", self.ang;
		print ("");
		return


if __name__ == "__main__":
    new_talker = Talker()
    new_talker.talk()

