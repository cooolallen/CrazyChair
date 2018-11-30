import Constants
import sys
import smtplib 
from email.mime.multipart 	import MIMEMultipart
from email.mime.text 		import MIMEText
from email.mime.image 		import MIMEImage

class PostOfficer(object):
	def __init__(self):
		self._server = self._server_run()

	def _server_run(self):
		#create server
		server=smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()
		# Login Credentials for sending the mail
		server.login(Constants.defaultParas['sender'], Constants.defaultParas['password'])

		return server

	def _get_body(self):
		body = MIMEMultipart() 
		# setup the parameters of the message
		# password 	=para.password
		# msg['From'] =para.my_email
		# msg['To'] 	=para.my_email
		body['From'] = Constants.defaultParas['sender']
		body['To'] = Constants.defaultParas['destination']
		body['Subject'] = Constants.defaultParas['subject']
		
		return body

	def send(self, msg=None, destination=None, subject=None):
		if msg is None:
			print('we cannot deliever the empty msg')
			return

		body = self._get_body()

		if destination is not None:
			body['To'] = destination

		if subject is not None:
			body['Subject'] = subject

		body.attach(MIMEText(msg, 'plain'))

		# send the message via the server.
		self._server.sendmail(body['From'], body['To'], body.as_string())
		print('email sended')

if __name__ == '__main__':
	test = PostOfficer()
	test.send(msg='hello world3')
	test.send(msg='hello world4')
