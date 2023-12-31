import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
try:
    from resource.variables import *
except ModuleNotFoundError:
    from variables import *
from os import path


def send_mail_success_execution(recipient_mail, message, filename=None):
    print('Sending email...')
    msg = MIMEMultipart()
    msg['From'] = USER_EMAIL
    msg['To'] = recipient_mail
    msg['Subject'] = "[Result] Remote Control Command"

    msg.attach(MIMEText(message, 'html'))

    if filename != None:
        image_extentions = {'.png','.jpg'}
        if filename.lower().endswith(tuple(image_extentions)):
            with open(filename, 'rb') as fp:
                img = MIMEImage(fp.read())
                img.add_header('Content-ID', '<image1>')
                msg.attach(img)
        elif filename.lower().endswith('.txt'):
            with open(filename, 'r', encoding='utf-8') as fp:
                file = MIMEText(fp.read(), 'plain')
                file.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(file)

    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(USER_EMAIL, USER_PASSWORD)
        text = msg.as_string()
        server.sendmail(USER_EMAIL, recipient_mail, text)
        server.quit()
        print("Email sent")
    except Exception as e:
        print(e)


def send_mail_failure_execution(recipient_mail, message):
    print('Failed to execute\nSending email...')
    msg = MIMEMultipart()
    msg['From'] = USER_EMAIL
    msg['To'] = recipient_mail
    msg['Subject'] = "[Result] Remote Control Command"

    msg.attach(MIMEText(message, 'html'))
    filename = path.dirname(path.abspath(__file__)) + "\\croc.jpg"
    with open(filename, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<image1>')
        msg.attach(img)
    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(USER_EMAIL, USER_PASSWORD)
        text = msg.as_string()
        server.sendmail(USER_EMAIL, recipient_mail, text)
        server.quit()
        print("Email sent")
    except Exception as e:
        print(e)
