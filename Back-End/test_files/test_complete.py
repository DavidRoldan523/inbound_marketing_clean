import pandas as pd
import numpy as np
import re
import dns.resolver
import socket
import smtplib

def verify_email(email):
    email = email.lower()
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        return 0
    try:
        records = dns.resolver.query(email.split('@')[1], 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        host_name = socket.gethostname()
    except Exception:
        return 0
    try:
        #SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(0)
        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(host_name)
        server.mail('me@domain.com')
        code, message = server.rcpt(str(email))
        server.quit()
    except Exception as e:
        return 0
    return 1

if __name__ == '__main__':
    list_emails = ['laam2005@gmail.com',
                   'andreson.albe@gmail.com',
                   'andrruiz40@gmail.com',
                   'andrruiz40@gmil.com']
    
    for email in list_emails:
        print(f'{email} || {verify_email(email)}')

 