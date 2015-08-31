# encoding:utf-8
import web
from web import form
from webapp.Common import Common
from webapp.pages.BasePage import BasePage
from webapp.logic.AuthorityManagement import AuthorityManagement


class Login(BasePage):
	"""
	登录页面
	"""


	require = form.regexp(r"\S/", '输入框不能为空')
	register_form = form.Form(
						form.Textbox('userName', description='用户名'),
						form.Password('password', description='密码'),
						form.Button("submit", type="submit", description=u"登录", html=u"登录"),
						)


	def GET(self):
		return Common.render.login(self.register_form())


	def POST(self):
		if self.register_form().validates():
			# 登陆验证
			userName = web.input().userName
			password = web.input().password
			if AuthorityManagement.login(userName, password):
				# 登录成功
				return web.seeother('/')
			else:
				# 登录失败
				return Common.render.login(self.register_form())
		else:
			# 输入错误
			print "输入错误"
			return Common.render.login(self.register_form())
