rosservice call /turtlesim1/clear

rosservice call /turtlesim1/reset
rosservice call /turtlesim1/spawn 7.5 5.5 0 ""
rosservice call /turtlesim1/turtle1/set_pen 255 255 0 3 OFF
rostopic pub -1 /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist -- '[5.0, 0.0, 0.0]' '[0.0, 0.0, 7.8]'
rostopic pub -1 /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, .0]' '[0.0, 0.0, 0.0]'

rostopic pub -1 /turtlesim1/turtle2/cmd_vel geometry_msgs/Twist -- '[5.0, 0.0, 0.0]' '[0.0, 0.0, 7.8]'
rostopic pub -1 /turtlesim1/turtle2/cmd_vel geometry_msgs/Twist -- '[.75, 0.0, .0]' '[0.0, 0.0, 0.0]'
rostopic pub -1 /turtlesim1/turtle2/cmd_vel geometry_msgs/Twist -- '[-1.5, 0.0, .0]' '[0.0, 0.0, 0.0]'

