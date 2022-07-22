---------------------------------------------|
1- Download and install VirtualBox           |
2- install Ubuntu 18.04.6                    |
3- Open Terminal from ubuntu                 |
---------------------------------------------|
#--- Setup your sources.list
 sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

#--- Set up your keys
 sudo apt install curl # if you haven't already installed curl curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

#--- Installation: 
sudo apt update

#4 Desktop Install: Everything in Desktop plus 2D/3D simulators and 2D/3D perception packages 
sudo apt install ros-noetic-desktop-full

#5 Desktop Install: Everything in ROS-Base plus tools like rqt and rviz
 sudo apt install ros-noetic-desktop

#6 ROS-Base: (Bare Bones) ROS packaging, build, and communication libraries. No GUI tools
 sudo apt install ros-noetic-ros-base

#7There are even more packages available in ROS. You can always install a specific package directly. 
sudo apt install ros-noetic-PACKAGE

#- e.g.
sudo apt install ros-noetic-slam-gmapping

#8 Environment setup
 source /opt/ros/noetic/setup.bash

#9 It can be convenient to automatically source this script every time a new shell is launched. These commands will do that for you.

echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc source ~/.bashrc

#10 Dependencies for building packages: 
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

#11 Initialize rosdep: 
sudo apt install python3-rosdep


