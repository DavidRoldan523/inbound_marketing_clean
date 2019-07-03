import pandas as pd
import numpy as np
import re
import dns.resolver
import socket
import smtplib
import time


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
    """
    try:
        #SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(0)
        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(host)
        server.mail('me@domain.com')
        code, message = server.rcpt(str(email))
        server.quit()
    except Exception:
        return 0
    """
    return 1

if __name__ == '__main__':
    initial_time = time.time()
    column_email_name = 'Email - Lead Capture Data'
    colum_status_email = 'StatusEmail'
    delimiter = ','
    dataframe = pd.read_csv('prueba_camila_corta.csv', engine="python", sep=delimiter, quotechar="'", error_bad_lines=False)
    dataframe.insert(dataframe.columns.get_loc(column_email_name) + 1, colum_status_email, 0)
    dataframe[colum_status_email] = dataframe[column_email_name].apply(verify_email)

    dataframe.to_csv('pandas_test.csv', index=False, header=True, sep=',')
    print(f'Success {time.time() - initial_time} seg')

 


