import math

def extract_distance(angle_deg : int,) -> float:
    """Extracts distance at the specified angle in degrees."""
    idx = int((angle_deg % 360) / (msg.angle_increment * (180 / math.pi)))
    if 0 <= idx < len(msg.ranges):
        val = msg.ranges[idx]
        if val and not math.isinf(val) and val > 0.01:
            return val
    return None


import subprocess
from time import sleep
import requests

def test_master() -> bool:
    try:
        requests.get("http://localhost:11311", timeout=0.5)
        return True
    except:
        return False

def start_master() -> subprocess.Popen[bytes]:
    process = subprocess.Popen(
        ['roslaunch', 'ydlidar_ros_driver', 'lidar_view.launch'],
        cwd='/home/rpi/ydlidar_ws/src/ydlidar_ros_driver/launch',
        stdout=subprocess.DEVNULL,  # or subprocess.PIPE if you want to read output
        stderr=subprocess.DEVNULL
    )

    # Wait for ROS master to become available
    for x in range(10):
        print("🔄 Waiting for ROS master...", x)
        if test_master():
            print("✅ ROS master is up!")
            break
        sleep(1)
    else:
        print("❌ Failed to detect ROS master.")
    return process

def stop_master(process : subprocess.Popen[bytes]):
    try:
        if not process:
            print("No process to terminate.")
            return
        process.terminate()
        process.wait(timeout=3)  # Wait for graceful shutdown
        print("✅ Process terminated gracefully.")
    except subprocess.TimeoutExpired:
        print("⏳ Timeout expired. Forcing kill...")
        process.kill()
        process.wait()
        print("🛑 Process killed.")
