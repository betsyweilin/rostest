# rostest
beginner 作为本地
另外一个作为远端主机,setup.sh作为环境参数
#!/bin/bash
export ROS_WS=/home/shunya/catkin_ws
source /opt/ros/kinetic/setup.bash
source $ROS_WS/devel/setup.bash
export PATH=$ROS_ROOT/bin:$PATH
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$ROS_WS
export ROS_MASTER_URI=http://192.168.10.21:11311
export ROS_HOSTNAME=192.168.10.157
export ROS_IP=192.168.10.157
exec "$@"
hostname 为lidar 

本地启动远端节点
roslaunch beginner  lidar.launch 
~/.ssh/config增加：
Host lidar
    HostName 192.168.10.157
    User shunya

/etc/hosts增加192.168.10.157  lidar




