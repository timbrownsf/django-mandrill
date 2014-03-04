from django.core.mail.message import EmailMessage

class MandrillMail(EmailMessage):
	alternative_subtype = "mandrill_message"

	def __init__(self, args):
		self.mandrill_args = args
		self.connection = None
	
	def send(self, fail_silently=False):
		return self.get_connection(fail_silently).send_messages([self])

class MandrillTemplateMail(EmailMessage):
	alternative_subtype = "mandrill_template"

	def __init__(self, template, content, args):
		self.mandrill_template_name = template
		self.mandrill_template_content = content
		self.mandrill_args = args
		self.connection = None

	def send(self, fail_silently=False):
		return self.get_connection(fail_silently).send_messages([self])
