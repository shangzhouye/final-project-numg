# Mini Golfer

*By Joshua Cohen, Yigitcan Comlek, Riley Knox, and Shangzhou Ye*

## Overview

A mini golfing robot. 

## How to use it

To launch Gazebo simulation, moveit and rviz:

- install moveit for melodic
- install sawyer moveit configuration package (it is included in the rethink_moveit.rosinstall file in the repo)
- launch `moveit.launch` (`moveit.launch` would launch the gazebo simulation, moveit configuration for sawyer, rviz, and move_group_python_interface node)
   - if using the real robot instead of simulation, set if_sim to be false

## Nodes

- `move_group_python_interface` node can move the end effector to a certain pose (position and orientation)
  - the target pose is currently hardcoded in the python node

## Project Proposal

### Description:
Our goal is to make the Baxter robot play Mini-golf. The robot hits a ball into a hole with the putter. The stretch goal of this project is to have a user interface commanding putter shots. 

### Equipment:
* Acrylic for sides and plane of the table
* Plane -$28 x 2
* Walls -$28
* Ball
* Golfball
* Putter (3d printed)
* Baxter Robot
* External Camera
* Camera Rig (3d printed)

### High-Level Overview:
#### Nodes:
For this project, we are planning on writing 5 nodes.
* Camera operation
This node helps the robot localize the ball & hole 
* Distance/angle calculation
Path planning in task space
* Trajectory planning
This node uses inverse kinematics to plan the trajectory of the robot
* Robot joint control
This node operates the joints on the robot
* Game Manager:
This node determines if the ball is in the hole, and acts as a “hub” for the program, calling the other nodes based on the success status check
#### 3rd Party Packages:
* Baxter
* Baxter_tools
* Baxter_gazebo
* OpenCV translator
#### New Concepts
* Velocity Control
* Path Planning
* Manufacturing 
  * 3D printing of gripper and cue (stick) ~ 2hrs of design
  * Laser Cutting ~30 min design 
  * Tablesaw ~30 min operation 

### Role Breakdown
* Josh
Mechanical - Assist in prototyping
Trajectory - Implement path following behavior on the robot
* Yido
Operation of joints - Make the joints move according to the trajectory that is planned
* Shang
Distance/angle calculation - Calculate the distance and the angles to the hole according to the location of the ball
Path planning in task space - Plan a path according to the location of the ball in the task space
* Riley
Mechanical - Design of putter/game space; fabrication of game space
Computer Vision - Identification of ball, hole, and game space

### Preferred Robot
* Sawyer:
 * Only 1 arm needed
 * Putting may require higher torque

