import os
import datetime
import subprocess

# time = 'hh:mm:ss'


def screenRecord(time, hardward_encoding=False):
    now = datetime.datetime.now()
    source_dir = os.path.dirname(os.path.abspath(__file__)) + "\\screenshots\\"
    os.makedirs(source_dir, exist_ok=True)
    filename = "ScreenRecord_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".mkv"
    filename = source_dir + filename
    if (hardward_encoding):
        subprocess.call(os.path.dirname(os.path.abspath(__file__)) +
                        "\\ffmpeg.exe -f gdigrab -framerate 60 -i desktop -c:v h264_nvenc -qp 0 -t "
                        + time + ' "' + filename + '"')
    else:
        subprocess.call(os.path.dirname(os.path.abspath(__file__)) +
                        "\\ffmpeg.exe -f gdigrab -framerate 60 -i desktop -t "
                        + time + ' "' + filename + '"')
    return filename
