# encoding:utf-8
import web
from webapp.db.DBUserInfo import DBUserInfo


class UserInfo:
	"""
	登陆用户的基本信息
	"""

	userName = ""  # 用户民
	authority = 1  # 用户权限
	
	
	def __init__(self, userName, authority):
		self.userName = userName
		self.authority = authority


	def __str__(self):
		return "用户名:%s 权限:%d" % (self.userName, self.authority)


	@classmethod
	def insert(self, userName, password):
		'''
		插入数据
		'''
		value = 0;
		if DBUserInfo.select(userName) == None:
			value = DBUserInfo.insert(userName, password)
		return value


	@classmethod
	def selectAll(self, userName):
		'''
		查找用户
		'''
		value = DBUserInfo.selectAll(userName)
		return value
	
	
	@classmethod
	def select(self, userName):
		'''
		查找指定用户
		'''
		value = DBUserInfo.select(userName)
		return value
