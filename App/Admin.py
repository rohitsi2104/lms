from App.Actor import Actor
from core.config import config_instance
class Admin(Actor):
	admin = {}
	min_email_length = config_instance.min_email_length
	min_password_length = config_instance.min_password_length
	def __init__(self, AdminDAO):
		self.sess_key = "admin"
		self.dao = AdminDAO
		self.route_url = "/admin/"