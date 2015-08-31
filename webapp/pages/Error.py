# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage

class Error(BasePage):
	"""
	出错页面
	"""

	def GET(self):
		errorMessage = Common.session.exception
		return Common.render.error(errorMessage.message)
