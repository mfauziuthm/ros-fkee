import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class TempDisplay(Node):
    def __init__(self):
        super().__init__('temp_display')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10)
    def listener_callback(self, msg):
        self.get_logger().info('Received temperature: "%f"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    temp_display = TempDisplay()
    rclpy.spin(temp_display)
    temp_display.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

