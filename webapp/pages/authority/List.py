# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage
from webapp.logic.AuthorityManagement import AuthorityManagement

class List(BasePage):
	"""
	用户一览
	"""
	
	text = ""
	authorityList = [];
	
	def GET(self):
		'''
		'''
		return Common.render.authority.list(self)
	
	
	def POST(self):
		'''
		'''
		# 获取用户列表
		self.text = web.input().text
		self.authorityList = AuthorityManagement.selectAll(self.text)
		return Common.render.authority.list(self)
