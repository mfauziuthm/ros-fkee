import rclpy #ROS2 Python client library
from rclpy.node import Node #ROS2 Node class
from std_msgs.msg import Float32 # Importing the Float32 message type from the standard ROS2 messages package

class TempSensor(Node): #Defining a new class TempSensor Node
    def __init__(self): #Constructor for the TempSensor class
        super().__init__('temp_sensor') #Calling the constructor of the parent Node class and giving this node the name 'temp_sensor'  
        self.publisher_ = self.create_publisher(Float32, 'temperature', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.current_temp = 24.5    #Initial temperature value

    def timer_callback(self):
        temp_msg = Float32()
        temp_msg.data = self.current_temp  # Simulated temperature value
        self.publisher_.publish(temp_msg)
        self.get_logger().info('Publishing: "%f"' % temp_msg.data)    
         # Simulate the room getting slightly warmer
        self.current_temp += 0.1

def main(args=None):
    rclpy.init(args=args) #Initialize the ROS2 Python client library
    temp_sensor = TempSensor() #Create an instance of the TempSensor class
    rclpy.spin(temp_sensor) #Keep the node running and processing callbacks
    temp_sensor.destroy_node() #Destroy the node when done
    rclpy.shutdown() #Shutdown the ROS2 client library
    
if __name__ == '__main__':    
    main() #Call the main function to start the node      

