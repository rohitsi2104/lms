from App.Actor import Actor
from core.config import config_instance
class User(Actor):
	id = 0
	name = ""
	lock = False
	min_email_length = config_instance.min_email_length
	min_password_length = config_instance.min_password_length
	min_name_length = config_instance.min_name_length
	user = {}

	def __init__(self, UserDAO):
		self.dao = UserDAO
		self.sess_key = "user" # session key