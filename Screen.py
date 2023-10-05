import cv2
import numpy as np
import pyautogui
import time


def screenRecord(filename, resolution, fps, end_time):
    codec = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    start_time = time.time()
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if time.time() - start_time >= end_time:
            break
    out.release()


def screenshot(filename):
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img),
                       cv2.COLOR_RGB2BGR)
    cv2.imwrite(filename, img)
