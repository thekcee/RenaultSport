#!/usr/bin/env python

import curses
import rospy
from race.msg import drive_param
from race.msg import pid_input


kp = 14.0
kd = 0.09
servo_offset = 5
prev_error = 0.0
vel_input = 25.0
error_scale = 10
angle = servo_offset


pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

def control(data):
	global angle
	##Your code goes here
	# 1. Scale the error
	#2. Apply the PID equation on error to compute steering
	#3. Make sure the steering value is within bounds for talker.py
	error = (error_scale * data.pid_error)
	v0 = -(kp * error + kd * (prev_error - error))
	#TODO: check this equation (how to get steering angle and deal with servo_offset
	angle = angle - (servo_offset - v0)
	
	
	
	if angle < - 100:
		angle = -100
	if angle > 100:
		angle = 100
	
	## END

	msg = drive_param()
	msg.velocity = vel_input
	msg.angle = angle
	pub.publish(msg)
	
	
def shutdown():
	rospy.loginfo("Stopping the car")
	msg = drive_param()
	vel_input = 0
	msg.velocity = vel_input
	msg.angle = angle
	pub.publish(msg)
	rospy.sleep(1)

if __name__ == '__main__':
	print("Listening to error for PID")
	kp = input("Enter Kp Value: " )
	kd = input("Enter Kd value: " )
	vel_input = input("Enter Velocity: ")
	angle = servo_offset
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)
	rospy.on_shutdown(shutdown)
	rospy.spin()
