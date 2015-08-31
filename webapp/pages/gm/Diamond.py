# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage


class Diamond(BasePage):
	"""
	
	"""
	


	def GET(self):
		'''
		'''
		return Common.render.gm.diamond(self)


	def POST(self):
		'''
		'''
		return Common.render.gm.diamond(self)
