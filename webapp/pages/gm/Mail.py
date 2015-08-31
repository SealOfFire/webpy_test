# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage


class Mail(BasePage):
	"""
	发送邮件的页面
	"""
	
	addressees = []  # 收件人列表


	def GET(self):
		'''
		'''
		return Common.render.gm.mail(self)


	def POST(self):
		'''
		'''
		# aa = web.input().add
		# bb = web.input().send
		urlParam = web.input(bid=None);
		if urlParam.bid == u"addAttachment":
			# 添加附件
			print "addAttachment"
		elif urlParam.bid == u"send":
			# 发送邮件
			print "send"
		
		
		return Common.render.gm.mail(self)
