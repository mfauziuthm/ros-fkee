import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TimedMover(Node):
    def __init__(self):
        super().__init__('timed_mover')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        # State tracking variables
        self.state_start_time = time.time()
        self.current_state = "FORWARD"  # Start by moving forward
        
        self.get_logger().info("Infinite loop timed_mover started!")
        self.get_logger().info("Moving FORWARD for 5 seconds...")

    def timer_callback(self):
        msg = Twist()
        # Calculate time spent in the CURRENT state
        elapsed_time = time.time() - self.state_start_time

        if self.current_state == "FORWARD":
            if elapsed_time <= 5.0:
                # Drive straight
                msg.linear.x = 0.5 
                msg.angular.z = 0.0
            else:
                # 5 seconds are up! Switch to TURN state and reset timer
                self.current_state = "TURN"
                self.state_start_time = time.time()
                self.get_logger().info("Turning LEFT for 1.5 seconds...")
                
        elif self.current_state == "TURN":
            if elapsed_time <= 1.5:  # Turn for 1.5 seconds (half the time of forward)
                # Turn left (positive angular Z)
                msg.linear.x = 0.0
                msg.angular.z = 1.0 
            else:
                # 1.5 seconds are up! Switch back to FORWARD and reset timer
                self.current_state = "FORWARD"
                self.state_start_time = time.time()
                self.get_logger().info("Moving FORWARD for 5 seconds...")

        # Publish the command
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    timed_mover = TimedMover()
    
    try:
        # Spin keeps the node running, triggering the timer_callback indefinitely
        rclpy.spin(timed_mover)
    except KeyboardInterrupt:
        # This block catches CTRL+C
        timed_mover.get_logger().info("Shutdown requested. Stopping robot...")
        
        # Send a final zero-velocity message so the robot doesn't run away!
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0
        timed_mover.publisher_.publish(stop_msg)
        
    finally:
        timed_mover.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()