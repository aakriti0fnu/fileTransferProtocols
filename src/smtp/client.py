

import smtplib
from email.message import EmailMessage

import sys

from utility.utils import timeit

msg = EmailMessage()
msg["From"] = 'aakriti.cse@gmail.com'
msg["To"] = 'aakriti.cse@gmail.com'

@timeit
def smtp_server_request(s):
    '''
    Please note that the send_message() function
    only ends when the transaction is completed on the server side,
    i.e. it only ends after DATA is ACK'd.
    So,timing from the client script is ok even though it is push(not pull) protocol.
    '''
    s.send_message(msg)
    pass

filename = sys.argv[1]
server = sys.argv[2]
retrieved_file = "retrieved_" + filename
msg.add_attachment(open(f'data/server/{filename}', "r").read(), filename=retrieved_file)
#no msg subject or body, to keep file transfer overhead lower.

s = smtplib.SMTP(server, 25)
