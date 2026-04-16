#include <iostream>
#include <string>
using namespace std;

class Robot {
private:
    string name;

public:
    Robot(string n) {
        name = n;
    }

    void greet() {
        cout << "Hello, I am robot " << name << "!" << endl;
    }
};

int main() {
    Robot myRobot("TurtleBot");
    myRobot.greet();
    return 0;
}