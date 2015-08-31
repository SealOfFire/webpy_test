# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage
from webapp.logic.UserInfo import UserInfo

class List(BasePage):
	"""
	用户一览
	"""
	
	userName = ""
	userInfoList = [];
	
	def GET(self):
		'''
		'''
		return Common.render.userInfo.list(self)
	
	
	def POST(self):
		'''
		'''
		# 获取用户列表
		userName = web.input().userName
		self.userInfoList = UserInfo.selectAll(userName)
		return Common.render.userInfo.list(self)
