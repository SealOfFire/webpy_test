# encoding:utf-8
from DBBase import DBBase
from webapp.db.Log import Logger
from utils.DBUtil import DBConn


class DBUserInfo(DBBase):
	"""
	用户信息表
	"""
	
	
	@classmethod
	def login(self, userName, password):
		'''
		用户登录
		'''
		Logger.info('DBUserInfo.login begin')
		# Logger.info('DBUserInfo.login begin')
		db = DBConn()
		sql = 'select count(*) from mgame_tool.user_info where user_name=%s and password=%s'
		rownum, db_res = db.query(sql, (userName, password))
		rownum += 0
		for row in db_res:
			if row[0] == 1:
				return True
				# Logger.info('DBUserInfo.login end')
			elif row[0] == 0:
				return False
				# Logger.info('DBUserInfo.login end')
			elif row[0] > 1:
				msg = 'DBUserInfo.login:有重复用户userName[%s]' % userName
				Logger.error(msg)
				raise Exception(msg);
		msg = 'DBUserInfo.login:用户数据错误userName[%s]' % userName
		Logger.error(msg)
		raise Exception(msg);
		# Logger.info('DBUserInfo.login end')


	@classmethod
	def changePassword(self, userName, afterPassword, beforePassword):
		'''
		修改用户密码
		'''
		Logger.info('DBUserInfo.changePassword begin')
		sql = ''' update mgame_tool.user_info set password=%s where user_name=%s and password=%s '''
		pass
		Logger.info('DBUserInfo.changePassword end')


	@classmethod
	def insert(self, userName, password):
		'''
		创建用户
		'''
		Logger.info('DBUserInfo.insert begin')
		sql = ''' insert into mgame_tool.user_info(user_name, password) values(%s,%s)'''
		db = DBConn()
		rownum, db_res = db.query(sql, (userName, password))
		return rownum


	@classmethod
	def select(self, userName):
		'''
		查找指定的用户
		'''
		returnValue = {}
		sql = ''' select * from mgame_tool.user_info where user_name=%s '''
		db = DBConn()
		rownum, db_res = db.query(sql, (userName))
		for row in 	db_res:
			temp = {}
			temp['userName'] = row[0]
			returnValue.append(temp)
		if rownum == 0:
			return None
		else:
			return returnValue;
	
	
	@classmethod
	def selectAll(self, userName=''):
		'''
		查询用户
		'''
		Logger.info('DBUserInfo.select begin')
		returnValue = []
		sql = ''' select * from mgame_tool.user_info '''
		where = ''' where user_name like %s '''
		rownum, db_res = None, None
		db = DBConn()
		if userName == '':
			rownum, db_res = db.query(sql)
		else:
			sql = sql + where
			rownum, db_res = db.query(sql, ('%' + userName + '%'))
		rownum += 0
		for row in 	db_res:
			temp = {}
			temp['userName'] = row[0]
			returnValue.append(temp)
		return returnValue;
