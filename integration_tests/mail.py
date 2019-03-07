# This file is a part of IoT-LAB client
# Copyright (C) 2019 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import email
import imaplib
import os
import time


EMAIL = os.environ.get('IOTLAB_EMAIL')
EMAIL_PASSWORD = os.environ.get('IOTLAB_EMAIL_PASSWORD')
IMAP = os.environ.get('IOTLAB_IMAP')
IMAP_PORT = os.environ.get('IOTLAB_IMAP_PORT')


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
