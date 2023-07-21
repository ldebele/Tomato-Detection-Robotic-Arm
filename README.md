# Tomato Detection Robotic Arm

## Table Contents
- Overview
- Getting Started
- Contributor
## Overview
Deep Learning based universal robotic arm (UR5) that utilized for the binning process of ripe and unripe tomatoes.

## Getting Started
### How to use this repository
- Make sure you have installed Python and some useful libraries/packages such as Tensorflow, Numpy, Matplotlib, OpenCV, etc.
- Make sure you have install ROS-Neotic in your pc and raspberry pi. [Follow ros-neotic installation](http://wiki.ros.org/noetic) 

### 1. On your PC (Node) 
1. Create a workspace in your computer and name it ur_ws.
```
mkdir -p ur_ws/src
cd ur_ws/src

# Copy scripts folder from ros_slave/ur_ws and past it into src folder.
cd ~/ur_ws

# checking dependencies
rosdep install --from-paths src --ignore-src --rosdistro neotic

# build 
catkin_make

# source this workspace (careful when also sourcing others)
cd ~/ur_ws
source devel/setup.bash
```

2. Add this to bash file in the master pc
```
export export ROS_MASTER_URI=http://localhost:11311/
export ROS_HOSTNAME=[SLAVE_IP]
export ROS_IP=[SLAVE_IP]
```
3. source bash file
```
source .bashrc
```
### 2. On your Raspberry pi (Master)
Make sure you have a version of Git higher that 2.25.0 on your raspberry pi.
1. Run the following command to clone only the ros_master folder from this repository to your pi.
```
git clone --no-checkout https://github.com/ldebele/Tomato-Detection-Robotic-Arm.git

cd Tomato-Detection-Robotic-Arm

# Initialize the folder
git sparse-checkout init --cone

# pick the folder ros_master and add it in the repo.
git sparse-checkout set ros_master
``` 

2. Create a workspace in your Raspberry Pi and names it ur_ws.
```
mkdir -p ur_ws/src
cd ur_ws/src

# Copy scripts folder from ros_master folder and past it into src folder.
cd ~/ur_ws

# checking dependencies
rosdep install --from-paths src --ignore-src --rosdistro neotic

# build 
catkin_make

# source this workspace (careful when also sourcing others)
cd ~/ur_ws
source devel/setup.bash
```

3. Add this to bash file on your raspberry pi.
```
export ROS_MASTER_URI=http://[MASTER IP]:11311/
export ROS_HOSTNAME=[MASTER_IP]
export ROS_IP=[MASTER_IP]
```
4. source bash file
```
source .bashrc
```
## Contributor
- `Lemi Debele`