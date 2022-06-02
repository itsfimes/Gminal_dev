
import os
os.system("pip install keyboard")
os.system("pip install mouse")

import time
import keyboard
import mouse

mouse_stuck = True


keyboard.send("windows+r")
time.sleep(2)
mouse.move(100, 100, absolute=False, duration=2)
keyboard.send("backspace")


keyboard.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
keyboard.send("enter")
