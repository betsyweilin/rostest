import rospy
from std_msgs.msg import String
from dashboard_msgs.msg  import Cmd

def dbcmd():
    command = Cmd()
    command.func_id = 1
    command.value = 0
    command.retry = 0
    

    
   
    #command.header.seq += 1
        # using rospy.Time means automatically getting sim time as appropriate
    #command.header.stamp = rospy.Time.now()
        # the odometry frame is set here
        # TODO: set a parameter for the odometry frame
    #command.header.frame_id = '{0}/odom'.format(self.ns)


    log(logfile, "dbcmd_feedback id=" + str(command.func_id) +"v="+ str(command.value) + "r="+ str(command.retry) )
    pub.publish(command)

def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    #pub cmd callback topic to dashboard
    pub = rospy.Publisher('dashboard_cmd', Cmd, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.1) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        dbcmd()
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass