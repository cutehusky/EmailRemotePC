import os
import time
import cv2
from shutil import move
import pyautogui
import datetime


def main():
    print(webcam_image())


def countdown(duration):
    while duration > 0:
        minutes, seconds = divmod(duration, 60)
        # \r = overwrite the previous line
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)
        duration -= 1


def screenshot(tmp=None):
    scrshot = pyautogui.screenshot()
    now = datetime.datetime.now()
    # file name: screenshot_YYYY-MM-DD_HH-MM-SS.png
    filename = "screenshot_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    source_dir = os.path.dirname(os.path.abspath(__file__)) + "/screenshots/"
    os.makedirs(source_dir, exist_ok=True)
    filename = "screenshots/" + filename
    scrshot.save(filename)
    return filename


def webcam_image(tmp=None):

    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    cap.release()

    now = datetime.datetime.now()
    filename = "webcam_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    source_dir = os.path.dirname(os.path.abspath(__file__)) + "\\webcam\\"
    os.makedirs(source_dir, exist_ok=True)
    filename = source_dir + filename
    cv2.imwrite(filename, frame)
    return filename


if __name__ == "__main__":
    main()
