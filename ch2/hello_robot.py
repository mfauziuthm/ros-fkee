class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am robot {self.name}!")

robot = Robot("TurtleBot")
robot.greet()