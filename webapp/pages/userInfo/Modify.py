# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage
from webapp.logic.UserInfo import UserInfo

class Modify(BasePage):
	"""
	用户信息编辑
	"""
	
	userName = ""
	password = ""
	confirmPassword = ""
	
	def GET(self):
		'''
		'''
		urlParam = web.input(un=None)
		self.userName = urlParam.un
		
		return Common.render.userInfo.modify(self)
	
	
	def POST(self):
		'''
		'''
		self.userName = web.input().userName
		self.password = web.input().password
		self.confirmPassword = web.input().confirmPassword
		# 验证输入项目
		if self.checkForm():
			if UserInfo.insert(self.userName, self.password) > 0:
				return web.seeother('/userInfo/list')
			else:
				return Common.render.userInfo.modify(self)
		else:
			return Common.render.userInfo.modify(self)
	
	
	def checkForm(self):
		'''
		输入表单验证
		'''
		if self.userName == "":
			return False
		if self.password == "":
			return False
		if self.confirmPassword == "":
			return False
		if self.password != self.confirmPassword:
			return False
		if UserInfo.select(self.userName) != None:
			return False
		return True
		
		
