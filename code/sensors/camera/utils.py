from .setup import hl, NOISE_THRESHOLD as _NOISE_THREASHOLD
from . import huskylib

def get_colors():
    colors = []
    blocks = hl.requestAll()
    if blocks:
        for b in blocks:
            colors.append(b.__dict__)
    return colors

def get_primary_color(NOISE_THREASHOLD=_NOISE_THREASHOLD):
    colors = get_colors()
    primary_color = 0
    largest_area = NOISE_THREASHOLD

    for color in colors:
        area = get_area(color)
        if area > largest_area:
            largest_area = area
            primary_color = color
    
    return primary_color

def get_center_of_color(color: huskylib.Block):
    return (color['x'] + color['width'] // 2, color['y'] + color['height'] // 2)

def get_area(color: huskylib.Block):
    return color['width'] * color['height']

screen_width = 320
screen_height = 240
def get_center_of_color_on_screen(color: huskylib.Block):
    center_x, center_y = get_center_of_color(color)
    return (center_x/screen_width,  center_y/screen_height  )