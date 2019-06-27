import re
import dns.resolver
import socket
import smtplib


class Email:
	def __init__(self, email, syntax, existence):
		self.email = email
		self.syntax = syntax
		self.existence = existence

	def verify_syntax(self):
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
		if match:
			return True
		else:
			return False

	def verify_domain(self):
		pass

	def verify_existence(self):
		pass

	def verify_email(self):
		if self.syntax:
			self.verify_syntax()
		self.existence = existence




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