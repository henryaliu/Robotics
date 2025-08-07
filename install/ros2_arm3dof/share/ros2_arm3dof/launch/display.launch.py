import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():
    # Get the urdf file
    urdf_file_name = 'arm_3_dof.urdf'
    urdf = os.path.join(
        get_package_share_directory('ros2_arm3dof'),
        'urdf',
        urdf_file_name)
    
    # Get the rviz config file
    rviz_config_file = os.path.join(
        get_package_share_directory('ros2_arm3dof'),
        'rviz',
        'arm_3_dof.rviz')

    # Read robot description from URDF file
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    # Robot state publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}],
        arguments=[urdf])

    # Joint state publisher GUI node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen')

    # RViz node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file])

    # Launch description
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])