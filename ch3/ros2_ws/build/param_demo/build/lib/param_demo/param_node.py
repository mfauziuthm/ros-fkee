import rclpy
from rclpy.node import Node

class SpeedController(Node):
    def __init__(self):
        super().__init__('speed_controller')
        
        # 1. Declare the parameter with a name and a default value
        self.declare_parameter('max_speed', 0.5)
        
        # Create a timer to constantly check and use the parameter
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        # 2. Get the current value of the parameter
        current_max_speed = self.get_parameter('max_speed').value
        
        # In a real robot, this is where you would enforce the speed limit
        self.get_logger().info(f'The robot speed limit is currently set to: {current_max_speed} m/s')

def main(args=None):
    rclpy.init(args=args)
    node = SpeedController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()