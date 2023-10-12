import imaplib
import email
import datetime
import time
import variables
import re

USER_EMAIL = variables.USER_EMAIL
USER_PASSWORD = variables.USER_PASSWORD
imap_address = variables.imap_address
imap_port = variables.imap_port


def main():
    while True:
        now = datetime.datetime.now()
        timestamp = '\n>> > >[ '+now.strftime("%H:%M:%S") + ' ]< < <<\n'
        print(timestamp)
        msg_list = get_mail_object()
        cmd_list = decode_mail(msg_list)
        if cmd_list != None:
            for cmd in cmd_list:
                print(cmd)
        time.sleep(10)


def login():
    mail = imaplib.IMAP4_SSL(imap_address, imap_port)
    print("Connected to gmail...")
    mail.login(USER_EMAIL, USER_PASSWORD)
    print("Logged in...")
    return mail


def get_mail_object(mail):

    # modifiable
    mailbox = 'inbox'  # types: inbox, sent, draft, trash, spam
    mail.select(mailbox)
    # types: ALL, UNSEEN, SEEN, ANSWERED, DELETED, UNDELETED, FLAGGED, UNFLAGGED, DRAFT, UNDRAFT
    # custom subject: '(SUBJECT "[subject here]")'
    _, data = mail.search(None, '(UNSEEN SUBJECT "[Remote Control Command]")')
    if (len(data[0].split()) == 0):
        mail.close()
        return None
    msg_list = []
    for num in data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        # data type: bytes, decode = utf-8
        msg = email.message_from_bytes(data[0][1])
        msg_list.append(msg)
        mail.store(num, '+FLAGS', '\\Seen')  # UNSEEN -> SEEN
    mail.close()
    return msg_list


def decode_mail(msg):
    cmd_list = []
    print('-------------------------')
    # print('From:', msg["From"])
    From = re.search(r'[\w\.-]+@[\w\.-]+', msg['From']).group()
    print('From:', From)
    print('Content:')
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            content = part.get_payload(decode=True).decode('utf-8')
            content = content.split('\r\n')
            for message in content:
                if message != '':
                    cmd_list.append(message)
                    print(message)
    return cmd_list  # one string or list of strings (unstripped)


if __name__ == "__main__":
    main()
