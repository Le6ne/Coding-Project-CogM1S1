from constants import *
from expyriment import io
import math as m

def wait_for_dot_click(correct_dot_idx, dot_positions, radius=DOT_RADIUS):
    mouse = io.Mouse(show_cursor=True)
    while True:
        button, (x, y) = mouse.wait()
        clicked_dot = None
        for idx, (dot_x, dot_y) in enumerate(dot_positions):
            dist = m.sqrt((x - dot_x) ** 2 + (y - dot_y) ** 2)
            if dist <= radius:
                clicked_dot = idx
                break
        if clicked_dot is not None:
            return clicked_dot == correct_dot_idx
