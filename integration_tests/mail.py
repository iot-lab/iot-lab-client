import email
import imaplib
import os
import time

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

EMAIL = os.environ.get('IOTLAB-EMAIL')
EMAIL_PASSWORD = os.environ.get('IOTLAB-EMAIL-PASSWORD')
IMAP = os.environ.get('IOTLAB-IMAP')
IMAP_PORT = os.environ.get('IOTLAB-IMAP-PORT')


def imap():
    M = imaplib.IMAP4_SSL(host=IMAP, port=IMAP_PORT)
    rv, data = M.login(EMAIL, EMAIL_PASSWORD)
    print((rv, data))

    rv, mailboxes = M.list()
    if rv != 'OK':
        print('error listing email')
        return
    rv, data = M.select('\"iot-lab integration\"')
    if rv != 'OK':
        print('error listing label iot-lab integration')
        return

    return M, data


def get_emails():
    M, data = imap()

    M.logout()

    return data


def get_email(i):
    M, data = imap()

    rv, data = M.fetch(i, '(RFC822)')
    if rv != 'OK':
        print("ERROR getting message", i)
        return

    raw_email = data[0][1].decode('utf-8')

    msg = email.parser.Parser().parsestr(raw_email)

    M.logout()

    return msg


def wait_email(callback):
    while True:
        emails = get_emails()
        for i in emails:
            msg = get_email(i)
            if callback(msg):
                return
        print('waiting for new email...')
        time.sleep(1)
