# Tomato Detection Robotic Arm
Deep Learning Based Tomato Detection Robotic Arm

### How to use this repository

- Make sure you have installed Python and some useful libraries/packages such as Tensorflow, Numpy, opencv, etc 


## Getting Started
- Make sure you have install ROS-Neotic in your pc and raspberry pi. 

    Follow ros-neotic installation 
[link](http://wiki.ros.org/noetic) 


### 1. PC
- Assuming your slave workspace is names as ur_ws, copy ros_slave/ur_ws/script folder from this repository and past it into ur_ws/src folder that you will create.
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
export ROS_HOSTNAME=[MASTER IP]
export ROS_IP=[MASTER IP]
```
3. source bash file
```
source .bashrc
```



### 2. Raspberry pi
Make sure you have a version of Git higher that 2.25.0 on your raspberry pi.
1. Run the following command to clone only the ros_master folder from this repository to your pi.
```
git clone --no-checkout https://github.com/ldebele/Tomato-Detection-Robotic-Arm.git

cd Tomato-Detection-Robotic-Arm

# Initialize the folder
git sparse-checkout init --cone

# pick the folder ros_master and add it in the repo.
git sparse-checkout set ros_master

git checkout @
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
export ROS_HOSTNAME=[SLAVE IP]
export ROS_IP=[SLAVE IP]
```
4. source bash file
```
source .bashrc
```
