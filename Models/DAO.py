from flask import current_app
from Models.DBDAO import DBDAO


class DAO():
	def __init__(self, app):
		self.db = DBDAO(app)


DAO_INSTANCE = DAO(current_app)