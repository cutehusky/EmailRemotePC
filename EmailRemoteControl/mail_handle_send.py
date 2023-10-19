import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import variables
from os import path

smtp_host = variables.smtp_host
smtp_port = variables.smtp_port
USER_EMAIL = variables.USER_EMAIL
USER_PASSWORD = variables.USER_PASSWORD


def main():
    pass

def send_mail_success_execution(recipient_mail, message, filename=None):
    print('Sending email...')
    msg = MIMEMultipart()
    msg['From'] = USER_EMAIL
    msg['To'] = recipient_mail
    msg['Subject'] = "[Result] Remote Control Command"

    msg.attach(MIMEText(message, 'html'))
    # no attachment -> send croc
    if filename == None:
        filename = path.dirname(path.abspath(__file__)) + "\\croc.jpg"
    # has binary attachment -> send image
    elif filename.lower().endswith('.png') or filename.lower().endswith('.jpg'):
        with open(filename, 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)
    else:
        crocpath = path.dirname(path.abspath(__file__)) + "\\croc.jpg"
        with open(crocpath, 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)
        with open(filename, 'r', encoding='utf-8') as fp:
            file = MIMEImage(fp.read(), 'plain', name=filename)
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
    print('Sending email...')
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


if __name__ == "__main__":
    main()
