from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the Sensor Node (Publisher)
        Node(
            package='node_temp_py',        # The package where the node lives
            executable='temp_sensor',    # The executable name (from setup.py)
            name='temperature_sensor',   # (Optional) Rename the node on the fly
            output='screen'              # Ensure the node's print statements show in the terminal
        ),
        
        # Launch the Display Node (Subscriber)
        Node(
            package='node_temp_py',
            executable='temp_display',
            name='thermostat_display',
            output='screen'
        )
    ])