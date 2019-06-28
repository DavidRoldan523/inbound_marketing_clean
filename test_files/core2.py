import re
import dns.resolver
import socket
import smtplib

addressToVerify = 'hdgomez1@hotmail.com'
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match is None:
   print('Bad Syntax')

records = dns.resolver.query(addressToVerify.split('@')[1], 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

# Get local server hostname
host = socket.gethostname()

# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()

server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail('me@domain.com')
code, message = server.rcpt(str(addressToVerify))
server.quit()

# Assume 250 as Success
if code == 250:
   print('Success')
else:
   print('Bad')