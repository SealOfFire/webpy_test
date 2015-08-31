# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage


class Index(BasePage):
	"""
	首页
	"""
	def GET(self):
		"""
		from webapp.logic.AuthorityManagement import AuthorityManagement
		AuthorityManagement.login("xus1", "aaa")
		print Common.session.userInfo
		BasePage.GET(self)
		"""
		name = 'Bob'
		# i = web.input(name=None)
		return Common.render.index(name)
	
	

