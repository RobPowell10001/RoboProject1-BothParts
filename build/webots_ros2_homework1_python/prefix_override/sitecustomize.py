import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/thor10001/Project1Parts1_2/project1_python/install/webots_ros2_homework1_python'
