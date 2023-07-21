# Tomato Detection Robotic Arm
Deep Learning Based Tomato Detection Robotic Arm

### How to use this repository

- Make sure you have installed Python and some useful libraries/packages such as Tensorflow, Numpy, opencv, etc 


### 1. PC
- Assuming your master universal robot workspace is names as ur_ws, download ur_ws/script folder from this repository and past it into ur_ws/src folder that you will create.

Follow ros-neotic installation
- http://wiki.ros.org/noetic/Installation/Ubuntu

    ```
    mkdir -p ur_ws/src
    cd ur_ws/src

    # Copy scripts folder from ur_ws and past it into src folder.

    cd ~/ur_ws

    # checking dependencies
    rosdep install --from-paths src --ignore-src --rosdistro neotic

    # build 
    catkin_make

    # source this workspace (careful when also sourcing others)
    cd ~/ur_ws
    source devel/setup.bash
    ```

### 2. Raspberry pi
```
    mkdir -p ur_ws/src
    cd ur_ws/src

    # Copy the files from pi past into ur_ws/src folder.
    cd ~/ur_ws

    # checking dependencies
    rosdep install --from-paths src --ignore-src --rosdistro neotic

    # build 
    catkin_make

    # source this workspace (careful when also sourcing others)
    cd ~/ur_ws
    source devel/setup.bash
    ```



Add this to bash file in the master pc
```
export export ROS_MASTER_URI=http://localhost:11311/
export ROS_HOSTNAME=[MASTER IP]
export ROS_IP=[MASTER IP]
```
then source bash file



add this to bash file of slave pc (raspberry pi in this context)
```
export ROS_MASTER_URI=http://[MASTER IP]:11311/
export ROS_HOSTNAME=[SLAVE IP]
export ROS_IP=[SLAVE IP]
```
then source bash file





