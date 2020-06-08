from pynput import keyboard
import time
import random
from pynput.keyboard import Controller
import threading
import sys
keep_running = True
times = 2


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.Key.f2},
    {keyboard.Key.shift, keyboard.Key.f2}
]

keyboard_control = Controller()
current = set()


def clicker():
    global keep_running
    while True:    
        while keep_running == True:
            print("f")
            keyboard_control.type('F')
            time.sleep(1)
        time.sleep(.5)

def execute(key):
    global keep_running
    global times
    time.sleep(0.3)
    print("\nRunning execute()\n")
    if times > 2:
        if (times % 2) == 0:
            keep_running = True
            times += 1
            print(times)
        else:
            keep_running = False
            times += 1
            print(times)
    else:
        if (times % 2) == 0:
            t1.start()
            times += 1
            print(times)
        else:
            keep_running = False
            times += 1
            print(times)




def on_press(key):
    print(f"Running on_press({key})")
    if any([key in COMBO for COMBO in COMBINATIONS]):
        print(f"  About to add {key}")
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            print("  About to run execute()")
            execute(key)

def on_release(key):
    print(f"Running on_release({key})")
    if any([key in COMBO for COMBO in COMBINATIONS]):
        print(f"  About to remove {key}")
        current.remove(key)
        print(f"   removed {key}")

t1 = threading.Thread(target=clicker) 


print("\nStarting to run listener\n")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
