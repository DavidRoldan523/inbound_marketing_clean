import pandas as pd
import modin.pandas as pd
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
    column_email_name = 'Correo'
    colum_status_email = 'StatusEmail'
    dataframe = pd.read_excel('Convergencia-Junio.xlsx')
    dataframe.insert(dataframe.columns.get_loc(column_email_name) + 1, colum_status_email, 0)
    dataframe[colum_status_email] = dataframe[column_email_name].apply(verify_email)
    
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print('Success')
 