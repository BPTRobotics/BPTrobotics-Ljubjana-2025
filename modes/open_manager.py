def start(ROUNDS = 3):
    from ..sensors import gyroscope
    from . import mode1, detect_direction, mode2, lidar_manager
    gyroscope.calibrate()
    gyroscope.INITIAL_DIRECTION.value = gyroscope.get_safe_pitch()


    mode1()
    detect_direction()
    mode2()
    for rnd in range(int(ROUNDS * 4 - 1)):
        mode1()
        mode2()

        print(rnd,"round has succesfully completed. 🚩")
    mode1(lidar_manager.START_DISTANCE.value)