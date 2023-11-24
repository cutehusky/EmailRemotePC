import os
import time
import cv2
from PIL import ImageGrab, Image
import datetime


def main():
    countdown(10)


def countdown(duration):
    while duration > 0:
        minutes, seconds = divmod(duration, 60)
        # \r = overwrite the previous line
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)
        duration -= 1


def shutdown():
    print("Shutting down in 10 seconds")
    countdown(10)
    os.system("shutdown -s -t 0")


def screenshot():
    scrshot = ImageGrab.grab()
    # file name: screenshot_YYYY-MM-DD_HH-MM-SS.png
    now = datetime.datetime.now()
    filename = "screenshot_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "..\\output\\screenshots\\")

    os.makedirs(source_dir, exist_ok=True)
    filename = source_dir + filename

    scrshot.save(filename)
    img = Image.open(filename)
    w, h = img.size
    if w > 960:
        # Image.NEAREST, Image.BILINEAR, Image.BICUBIC, Image.LANCZOS
        img = img.resize((int(w/2), int(h/2)), Image.LANCZOS)
    img.save(filename)

    return filename


def webcam_image():

    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    now = datetime.datetime.now()
    filename = "webcam_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"

    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "..\\output\\webcam\\")

    os.makedirs(source_dir, exist_ok=True)
    filename = source_dir + filename

    cv2.imwrite(filename, frame)

    cap.release()
    cv2.destroyAllWindows()
    return filename


if __name__ == "__main__":
    main()
