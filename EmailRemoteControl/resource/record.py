import os
import datetime
import subprocess

# time = 'hh:mm:ss'
# crf 0 - 51
def screen_record(time, crf=28, hardward_encoding=False):
    print("Recording...")
    now = datetime.datetime.now()
    source_dir = os.path.dirname(os.path.abspath(__file__)) + "\\screenshots\\"
    os.makedirs(source_dir, exist_ok=True)
    filename = "ScreenRecord_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".mkv"
    filename = source_dir + filename
    if (hardward_encoding):
        subprocess.call("ffmpeg -hide_banner -loglevel error -hwaccel cuda -f gdigrab -framerate 60 -i desktop -crf " + str(crf) + " -fs 25M -c:v h264_nvenc -t "
                        + time + ' "' + filename + '"')
    else:
        subprocess.call("ffmpeg -hide_banner -loglevel error -f gdigrab -framerate 60 -i desktop -crf " + str(crf) + " -fs 25M -t "
                        + time + ' "' + filename + '"')
    return filename

def webcam_record(time, crf=28, hardward_encoding=False):
    print("Recording...")
    now = datetime.datetime.now()
    source_dir = os.path.dirname(os.path.abspath(__file__)) + "\\screenshots\\"
    os.makedirs(source_dir, exist_ok=True)
    filename = "WebcamRecord_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".mkv"
    filename = source_dir + filename
    if (hardward_encoding):
        subprocess.call("ffmpeg -hide_banner -loglevel error -hwaccel cuda -f vfwcap -i 0 -framerate 60 -crf " + str(crf) + " -fs 25M -c:v h264_nvenc -t "
                        + time + ' "' + filename + '"')
    else:
        subprocess.call("ffmpeg -hide_banner -loglevel error -f vfwcap -i 0 -framerate 60 -crf " + str(crf) + " -fs 25M -t "
                        + time + ' "' + filename + '"')
    return filename

# q 1 - 31
def screenshot(q = 2):
    print("Recording...")
    now = datetime.datetime.now()
    source_dir = os.path.dirname(os.path.abspath(__file__)) + "\\screenshots\\"
    os.makedirs(source_dir, exist_ok=True)
    filename = "ScreenShot_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    filename = source_dir + filename
   
    subprocess.call('ffmpeg -hide_banner -loglevel error -f gdigrab -i desktop -frames:v 1 -q:v ' + str(q) + ' "' + filename + '"')
    return filename

# q 1 - 31
def webcam_shot(q = 2):
    print("Recording...")
    now = datetime.datetime.now()
    source_dir = os.path.dirname(os.path.abspath(__file__)) + "\\screenshots\\"
    os.makedirs(source_dir, exist_ok=True)
    filename = "WebcamShot_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    filename = source_dir + filename
   
    subprocess.call('ffmpeg -hide_banner -loglevel error -f vfwcap -i 0 -frames:v 1 -q:v ' + str(q) + ' "' + filename + '"')
    return filename