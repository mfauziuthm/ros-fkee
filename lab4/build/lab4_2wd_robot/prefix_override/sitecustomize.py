import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mfauzi/lab-activity/lab4_g/install/lab4_2wd_robot'
