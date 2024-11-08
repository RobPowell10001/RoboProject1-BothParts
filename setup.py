from setuptools import find_packages, setup

package_name = 'project1_python'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/project1_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/Part2MapDay.wbt']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/Part2MapNight.wbt']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/BrunoFloor1.wbt']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/BrunoFloor1DoorsClosed.wbt']))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/turtlebot_webots.urdf',
    'resource/ros2control.yml',
]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Monica Anderson-UA',
    maintainer_email='anderson@ua.edu',
    description='Simulation for cs460/560 Project 1',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],    
        'console_scripts': ['project1_python = project1_python.project1_python:main']
    },

)
