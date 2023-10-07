import os
import time
import pyautogui
import datetime


def main():
    screenshot()
    print("Screenshot taken")


def countdown(duration):
    while duration > 0:
        minutes, seconds = divmod(duration, 60)
        # \r = overwrite the previous line
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)
        duration -= 1


def screenshot(tmp = None):
    scrshot = pyautogui.screenshot()
    now = datetime.datetime.now()
    #file name: screenshot_YYYY-MM-DD_HH-MM-SS.png
    filename = "screenshot_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")
    filename = "screenshots/" + filename
    scrshot.save(filename)
    return filename

if __name__ == "__main__":
    main()