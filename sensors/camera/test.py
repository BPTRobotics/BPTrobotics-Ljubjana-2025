from .utils import get_center_of_color_on_screen, get_primary_color

import time
while True:
    primary_color = get_primary_color()
    if primary_color:
        x_center, y_center = get_center_of_color_on_screen(primary_color)
        print(primary_color['ID'],
              f"({x_center:.2f}, {y_center:.2f})")
    else:
        print("No colors detected")
    time.sleep(.5)