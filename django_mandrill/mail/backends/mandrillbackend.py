from django.core.mail.backends.base import BaseEmailBackend
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

import threading
import mandrill

class EmailBackend(BaseEmailBackend):
	def __init__(self, *args, **kwargs):
		api_key = getattr(settings, "MANDRILL_API_KEY", None)
		if api_key is None:
			raise ImproperlyConfigured("missing MANDRILL_API_KEY")

		self.mandrill = mandrill.Mandrill(api_key)
		self._lock = threading.RLock()
		super(EmailBackend, self).__init__(*args, **kwargs)
	
	def send_messages(self, email_messages):
		if not email_messages:
			return

		num_sent = 0
		with self._lock:
			for message in email_messages:
				sent = self._send(message)
				if sent:
					num_sent += 1

		return num_sent

	def _send(self, message):
		try:
			subtype = getattr(message, 'alternative_subtype', None)
			f = {
				'mandrill_message': self._send_message,
				'mandrill_template': self._send_template,
			}.get(subtype, self._send_raw)
			f(message)
		except:
			if not self.fail_silently:
				raise
			return False
		return True

	def _send_raw(self, message):
		if not message.recipients():
			return False
		self.mandrill.messages.send_raw(message.message().as_string())
		return True

	def _send_template(self, message):
		self.mandrill.messages.send_template(
			message.mandrill_template_name,
			message.mandrill_template_content,
			message.mandrill_args,
		)
		return True

	def _send_message(self, message):
		self.mandrill.messages.send(message.mandrill_args)
		return True
