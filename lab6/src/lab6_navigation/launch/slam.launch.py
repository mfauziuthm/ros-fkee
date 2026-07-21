import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # Locate the slam_toolbox package share directory
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')

    # Use the online asynchronous SLAM launch provided by slam_toolbox.
    # This mode is suitable for real-time mapping during teleoperation.
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(slam_toolbox_dir, 'launch', 'online_async_launch.py')
        ),
        launch_arguments={
            # Synchronize SLAM timestamps with the Gazebo simulation clock
            'use_sim_time': 'true',
        }.items(),
    )

    return LaunchDescription([
        slam_launch,
    ])
