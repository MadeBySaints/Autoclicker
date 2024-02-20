from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import time

# Create mouse controller
mouse = Controller()

# Global flags to control the clicking loop
stop_clicking = False
pause_clicking = False

# Function to handle key presses
def on_press(key):
    global stop_clicking, pause_clicking
    if key == kill_switch:
        stop_clicking = True
        return False  # Stop listener
    elif key == pause_switch:
        pause_clicking = not pause_clicking  # Toggle pause

# Function to perform the mouse click with user-defined timings and repetitions
def click_mouse(click_duration, wait_time, repeat):
    global stop_clicking, pause_clicking
    count = 0
    while not stop_clicking and (repeat == 0 or count < repeat):
        while pause_clicking:  # Pause loop
            time.sleep(0.1)  # Check every 0.1 seconds if still paused
        mouse.press(Button.left)
        time.sleep(click_duration / 1000)  # Convert to seconds
        mouse.release(Button.left)
        time.sleep(wait_time / 1000)  # Convert to seconds
        count += 1
    print("Autoclicker stopped.")

# Prompting user for configuration
wait_time = float(input("Enter time in ms to wait between clicks: "))
click_time = float(input("Enter time in ms click is held down: "))
repeat = int(input("Enter number of times to repeat click (0 for infinite until 'K' is pressed): "))

# Setting up the control keys
kill_switch = KeyCode.from_char('k')
pause_switch = KeyCode.from_char('p')

print("Autoclicker started. Press 'P' to pause/resume, 'K' to stop.")
# Start the key listener in a non-blocking manner
with Listener(on_press=on_press) as listener:
    click_mouse(click_time, wait_time, repeat)
