import imaplib
import email
import datetime
import time


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


def get_mail_object():

    USER_EMAIL = 'dummymailbox5186@gmail.com'
    USER_PASSWORD = "omwv msnm mxbx wllh"
    host_address = 'imap.gmail.com'
    host_port = 993  # SSL 993, TLS 143

    mail = imaplib.IMAP4_SSL(host_address, host_port)
    print("Connected to gmail...")
    mail.login(USER_EMAIL, USER_PASSWORD)
    print("Logged in...")

    # modifiable
    mailbox = 'inbox'  # types: inbox, sent, draft, trash, spam
    mail.select(mailbox)
    print(f'Current mailbox: {mailbox}')

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
        mail.store(num, '+FLAGS', '\\Seen') #UNSEEN -> SEEN
    mail.close()
    return msg_list

def decode_mail(msg):
    cmd_list = []
    print('-------------------------')
    print('From:', msg["From"])
    print('Content:')
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            content = part.get_payload(decode=True).decode('utf-8')
            cmd_list.append(content)
            print(content)
    return cmd_list # one string or list of strings (unstripped)

if __name__ == "__main__":
    main()
