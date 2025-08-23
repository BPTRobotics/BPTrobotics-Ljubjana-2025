from . import direction_manager
from ..control import motor
from ..sensors import lidar
from time import sleep
from . import lidar_manager
from ..control import servo

from ..sensors import camera

from .. import LCD

from ..Button import wait_for_button_press

def start(DISTANCE_ = 1):
    global lidar_manager
    motor.set_speed(1)

    hot_degrees = []
    wasTheLastHot = False
    middle_degree = None
    isObject = False

    lidar_range = 20

    pitch_diff = 0

    steer_by = 180

    motor.backward()
    while True:
        wait_for_button_press()
        if lidar_manager.msg:
            primary_color = camera.get_primary_color()
            if primary_color:
                middle_range = 180+pitch_diff
                for degree_to_read in range(int(middle_range - lidar_range),int(middle_range + lidar_range)):
                    distance = lidar.utils.extract_distance(
                        degree_to_read,
                        lidar_manager.msg
                    )
                    closest_distance = DISTANCE_

                    if distance and distance < closest_distance:
                        hot_degrees.append(degree_to_read)
                        wasTheLastHot = True
                        isObject = True
                        closest_distance = distance
                    if wasTheLastHot and distance and distance > DISTANCE_:
                        middle_degree = sum(hot_degrees) / len(hot_degrees)
                        hot_degrees = []
                        wasTheLastHot = False
                        color_id = primary_color['ID']
                        if color_id == 1:
                            augmented_direction = middle_degree-180-steer_by
                            LCD.set_mode(3)
                        elif color_id == 2:
                            augmented_direction = middle_degree-180+steer_by
                            LCD.set_mode(2)
                        else:
                            raise ValueError("Unknown color ID")
                        normaized_direction = min(max(-1, ( augmented_direction )), 1)
                        servo.safe_steer( normaized_direction )
                        print(f"MODE (3): Steering to {middle_degree:.2f}°")

                        pitch_diff = direction_manager.get_pitch_difference()
                
                lidar_manager.printall(lidar_manager.msg)
            else:
                print("No object detected by camera")
                isObject = False
                LCD.set_mode(0)

            motor.backward()
            if not isObject:
                pitch_diff = direction_manager.keep_direction()
            isObject = False
        else:
            motor.stop()
            continue
        
        sleep(0.05)
    motor.stop()