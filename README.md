
# BPT Robotics – Engineering Documentation




WRO Future Engineers – Slovenia 2025

##### **Team name:** BPT Robotics
##### **Members:**
- **Boldizsár Szakács - Békési** *- software developer, algorithm manager, sensor data processing*
- **Péter Márkus** *- mechanical design, assembly, 3D printing and prototyping, electronic design*
- **Tibor Bogar** - *electronics, cabling*

**Country:** Hungary
**Category:** WRO Future Engineers
**Competition location:** Slovenia, Ljubljana
**Date:** 2025, 2 - 5 of September


## 1. Team introduction
BPT Robotics is a young robotics team of three, born from a passion for technology, robotics and innovation. We all bring different strengths to the work together:
Boldizsár is the controller of programming logic and artificial intelligence, who builds the robot's brain.
Peti is a master of mechanical design and structural engineering, ensuring a stable and reliable frame, from CAD designs to 3D printed elements.
Tibi is an expert in precision electronics connections, ensuring that all hardware components communicate seamlessly and receive the proper power supply.
Our robot performed well in the Hungarian qualifiers, and thanks to this, we qualified for the 2025 WRO competition in Slovenia. Our goal is to present a technological solution that shows that anything can be achieved with a small team and limited resources. Although the Hungarian round did not start absolutely smoothly, we managed to make it to Slovenia. Gathering our experience from the competition, we rethought the entire robot and redesigned it in less than 3 months. Our motivation is to create a better world for our future children and grandchildren, so that we can participate in such big events of robotics at a young age.

## 2. The task
The challenge for the WRO Future Engineers category is to develop a fully autonomous robot that can navigate a changing obstacle course without human intervention. The robot:
must independently explore their environment,
must recognize and avoid obstacles,
must make decisions based on visual cues (such as color codes and walls),
you need to reach your destination via the shortest and most efficient route possible.
This task is a mechanical, electronic and software development challenge at the same time, as the robot has to process and react to complex data in real time. Another challenge during the preparation was that the robot had to be within a certain limit (300 x 200 x 300 mm) and could not exceed a weight limit of 1.5 kg. We started the work after a thorough planning. Initially, we thought about the structure and operation of the robot based on the experience gained so far. Later, Boldizsár started to do the programming part and integrate the software with the appropriate operating system. Initially, he did the Open challenge, refined it, and developed it, and when it worked perfectly, he supplemented it with the Obstacle challenge. After a lot of testing, our robot was created.

## 3. Robot concept
Our robot is a four-wheeled, back-wheel drive, back-wheel steering platform that we designed to be stable, modular, and easy to repair.
The main goal was to create a system that is capable of real-time decision-making with minimal latency. Our robot, has both a driven and steered rear axle, allowing for the most precise maneuvering possible.
Therefore, the main control unit is a Raspberry Pi 4 4GB model B, which runs the control program written in Python.

**Main features of the system:**
- **Husky Lens** camera for fast color recognition.
- YDLIDAR X4 Pro for 360° environmental mapping, which provides accurate data up to a distance of 10 meters. (which is enough)
- **GY-BNO085** IMU for precise heading and movement correction.
- **L298N** motor controller, which controls the drive motor with PWM control.
- **PCA9685**, this rotates our drive shaft for precise maneuvering

The core of the concept is the modular structure: any component can be quickly replaced, and the frame design allows for later expansions (for example, installing more powerful motors or new sensors).

## 4. Hardware details
[here comes the electronic picture that batteries -> bucks -> …]
| Component             | Function                                                       | Comment                  | Justification                                                                 |
|-----------------------|----------------------------------------------------------------|--------------------------|-------------------------------------------------------------------------------|
| Raspberry Pi 4 (4GB)  | Central control, data processing                               | Running Python code      | It's proven, it works well, although it's a bit slow, so we plan to switch to Pi5 next year. |
| L298N motor controller| Driven motor control                                           | PWM signal-based         | Cheap, works well                                                             |
| PCA9685               | Control of the rotation of the driven shaft                    |                          | There was a lot of it and it works well                                       |
| MG995                 | Rotating the driven shaft                                      | Metal metatarsal         | Because it is very powerful and even a little electricity is not enough for it |
| Blue TT motorcycle    | Drive of the driven axle produces more torque than the front-wheel drive, thus providing greater speed against the small wheel. | Metal metatarsal         | Because it is easier to handle than other engines in this price range.        |
| PixyCam2.1            | Color recognition                                              | Direct USB communication | Because it provides a very fast image, and color detection is already implemented by default |
| YDLIDAR X4 Pro        | 360° mapping, guidance, precise location                       | 10 m range               | Because at the moment of purchase, there was strong documentation.            |


## 5. Software architecture
[here you can find out how the sensors communicate with the pi]
Our developer decided to try a new approach into the sensor combination, which he called the **"module system"**, where he splits the software into different modules.

For example, when  the robot starts, it uses the lidar for navigation of distances and gyroscope to ensure the full forward direction he calls this state **"module 1"**. Then, when the robot approaches a corner, and needs to change its direction, then it turns off the lidar (since there's no need for that), and turns by only the data of the gyroscope. That state is called **"module 2"**. Then it changes between these modules.

### **Modules:**
##### **OPEN CHALLENGE's modules:**

##### **OBSTACLE CHALLENGE's modules:**
```
read LIDAR distance
read camera color
read gyro heading

IF obstacle detected (distance < safe_limit):
IF camera sees red:
turn left
ELSE IF camera sees blue:
turn right
ELSE:
stop, then go around slowly
ELSE:
move forward straight

correct direction with gyro
```


### **Download the repository**
**Clone the repository:**
`bash
git clone https://github.com/BPTRobotics/BPTRobotics-Ljubjana-2025.git
cd BPTrobotics-Ljubjana-2025`

**Download dependencies:**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip
pip install -r requirements.txt

Run the robot:
bash
python3 -m WRO.main
```
**Unit module tests**
```
python3 -m WRO.control.servo.test
python3 -m WRO.control.motor.test
python3 -m WRO.sensors.camera.test
python3 -m WRO.sensors.lidar.test
python3 -m WRO.sensors.gyroscope.test
```
**Compatibility**
Only compatible with `Ubuntu 20.04.5 Server`. (available in the `Raspberry PI Imager`)
[PI Imager -> Other Os -> Ubuntu 20.4.5 LTS]

## 6. Development 
##### **Transfer of previous experiences:**
Our previous robot was too heavy (in terms of weight) so we reduced its weight with 3D printed models and fewer components (Lidar instead of many ultrasonic sensors)
The batteries didn't last long, the power was low, so we used twice as many (i.e. 6) batteries.
Instead of an ultrasonic sensor, we use lidar, so we can see 360 ​​degrees
Instead of a USB webcam, we use a more professional camera, thus facilitating a more accurate solution to the obstacle challenge.
faster and more accurate gyroscope for more precise control and avoidance of unnecessary turns
Concept development – first CAD models and sensor placement.
First prototype – basic mechanical structure and motor control.
Sensor integration – Connecting LIDAR, PixyCam and IMU.
Algorithm development – writing navigation and obstacle avoidance code.
Fine tuning – testing and error correction on the test track.
Pre-competition calibration – sensor adjustments, mechanical repairs.

## 8. Innovations
Real-time sensor fusion, which combines data from LIDAR and PixyCam.
Energy-efficient motor control, which provides longer operating time and therefore requires less battery power.
Quick module replacement option(modularity) to eliminate errors during the competition and for quick and easy assembly.
development of componentsSince we have lidar and a more professional camera, we can solve both the open and obstacle challenges much more easily and accurately.

## 9. Future plans
Switching to Raspberry Pi 5 for faster processing. Since we want to process as much and as accurate data as possible, a fast controller is also important
Implementation of SLAM algorithm to improve mapping.
Designing a lighter, yet stronger frame. If it were possible to make the robot frame from a strong, yet lightweight sheet metal, that would be the best because it would be both lightweight and durable.
Better and longer battery capacity with less weight. Although it can withstand a full test day, it would be nice if it could not only withstand it, but also retain power and when the battery is low, the power would not drop, the engine would not slow down
