# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage


class Gold(BasePage):
	"""
	
	"""
	


	def GET(self):
		'''
		'''
		return Common.render.gm.gold(self)


	def POST(self):
		'''
		'''
		return Common.render.gm.gold(self)
