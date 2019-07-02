import re
import dns.resolver
import socket
import smtplib


class Email:
	def __init__(self, email):
		self.email = email

	def verify_email(self):
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
		if match == None:
			return False
		
		try:
			records = dns.resolver.query(self.email.split('@')[1], 'MX')
			mxRecord = records[0].exchange
			mxRecord = str(mxRecord)

			# Get local server hostname
			host = socket.gethostname()

			# SMTP lib setup (use debug level for full output)
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.set_debuglevel(0)

			# SMTP Conversation
			server.connect(mxRecord)
			server.helo(host)
			server.mail('me@domain.com')
			code, message = server.rcpt(str(self.email))
			server.quit()
		except Exception as e:
			return e

		# Assume 250 as Success
		if code == 250:
			return True
		else:
			return False
		




