import pyautogui as pg
import os
import time

def capture(number=1, delay=0):
    # "number" is the number of images to be captured
    # "delay" is the delay in seconds between each capture.
    # If no arguments are given, the function will capture one image
    # spontaneously.

    # clear images in "input" directory
    os.system("rm input/*.jpg")

    # initialise images index
    file_index = 0

    for i in range(number):
        # wait for specified delay (seconds)
        time.sleep(delay)
        # Call shell command to capture image and save it in JPG 
        # format inside "input" directory.
        os.system("scrot input/image" + str(file_index) + ".jpg")
        # increase file_index for next image capture
        file_index += 1

# accelerate the car in Carla simulator
def accelerate():
    pg.keyDown('w')

# stop accelerating the car in Carla simulator
def stop_accelerate():
    pg.keyUp('w')

# release control of the car
def release_control():
    # release all pressed keys
    pg.keyUp('w')

# code to run when this file is executed
if __name__ == '__main__':
    time.sleep(5)
    accelerate()
    capture(10, 2)
    stop_accelerate()

    release_control()