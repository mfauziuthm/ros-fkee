import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TimedMover(Node):
    def __init__(self):
        super().__init__('timed_mover')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("Timed mover starting in 2 seconds...")
        time.sleep(2.0) # Give Gazebo a moment to settle
        self.execute_sequence()

    def execute_sequence(self):
        msg = Twist()

        # 1. Move forward for 5s
        self.get_logger().info("Moving forward (5s)...")
        msg.linear.x = 0.5 
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        time.sleep(5.0)

        # 2. Turn left for 1s
        self.get_logger().info("Turning left (1s)...")
        msg.linear.x = 0.0
        msg.angular.z = -1.0 # Negative angular Z turns left (counter-clockwise)
        self.publisher_.publish(msg)
        time.sleep(3.0)

        # 3. Move forward for 3s
        self.get_logger().info("Moving forward (3s)...")
        msg.linear.x = 0.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        time.sleep(3.0)
        
        # 4. Turn right for 1s
        self.get_logger().info("Turning right (1s)...")
        msg.linear.x = 0.0
        msg.angular.z = 1.0 # Positive angular Z turns right (clockwise)
        self.publisher_.publish(msg)
        time.sleep(3.0)
        
        # 5. Move forward for 5s
        self.get_logger().info("Moving forward (5s)...")
        msg.linear.x = 0.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        time.sleep(5.0)

        # 6. Stop completely
        self.get_logger().info("Sequence complete. Stopping.")
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TimedMover()
    rclpy.shutdown()

if __name__ == '__main__':
    main()