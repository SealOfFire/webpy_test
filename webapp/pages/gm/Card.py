# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage


class Card(BasePage):
	"""
	
	"""
	


	def GET(self):
		'''
		'''
		return Common.render.gm.card(self)


	def POST(self):
		'''
		'''
		return Common.render.gm.card(self)
