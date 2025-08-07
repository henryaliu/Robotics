# ROS2 3-DOF Robotic Arm

This package contains a 3-DOF (3 Degrees of Freedom) robotic arm model for ROS2, complete with URDF description and RViz visualization with movement sliders. 

## Features

- 3-DOF robotic arm with revolute joints
- Joint control via GUI sliders
- Real-time visualization in RViz
- Proper ROS2 package structure

## Requirements

Make sure you have ROS2 Kilted installed and the following packages:

```bash
sudo apt update
sudo apt install ros-$ROS_DISTRO-robot-state-publisher \
                 ros-$ROS_DISTRO-joint-state-publisher \
                 ros-$ROS_DISTRO-joint-state-publisher-gui \
                 ros-$ROS_DISTRO-rviz2 \
                 ros-$ROS_DISTRO-urdf \
                 ros-$ROS_DISTRO-xacro
```

## Build Instructions

1. Clone/navigate to your workspace:
```bash
cd ~/your_ros2_workspace/src/ros2_arm3dof
```

2. Build the package:
```bash
cd ~/your_ros2_workspace
colcon build --packages-select ros2_arm3dof
```

3. Source the workspace:
```bash
source install/setup.bash
```

## Running the Simulation

Launch the complete visualization with interactive joint control:

```bash
ros2 launch ros2_arm3dof display.launch.py
```

This will open:
- RViz2 with the robotic arm visualization
- Joint State Publisher GUI for controlling the joints

## Usage

1. **Joint Control**: Use the Joint State Publisher GUI sliders to control each joint:
   - `joint1`: Base rotation (-180° to +180° for full circular motion)
   - `joint2`: Shoulder joint (-90° to +90°) 
   - `joint3`: Elbow joint (-115° to +115°)

2. **Visualization**: The arm is displayed in RViz with:
   - Purple and black colored links
   - TF axes showing joint freedoms
   - Grid for spatial reference

## File Structure

```
ros2_arm3dof/
├── CMakeLists.txt         # Build configuration
├── package.xml            # Package dependencies and metadata
├── README.md              # This
├── launch/
│   └── display.launch.py  # Launch file for complete setup
├── urdf/
│   └── arm_3_dof.urdf     # Robot description
└── rviz/
    └── arm_3_dof.rviz     # RViz configuration
```

## Robot Description

The robotic arm consists of:
- **Base Link**: Black cylindrical base 
- **Link 1**: Purple box section 
- **Link 2**: Black box section 
- **Link 3**: Purple box section
- **End Effector**: Black sphere 
