import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mfauzi/ros-fkee/ch4/ros2_ws/install/my_robot_description'
