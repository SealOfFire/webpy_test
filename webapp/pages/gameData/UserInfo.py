# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage

class UserInfo:
	'''
	'''
	
	def GET(self):
		return Common.render.gameData.userInfo(self)


	def POST(self):
		return Common.render.gameData.userInfo(self)
