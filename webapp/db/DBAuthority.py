# encoding:utf-8
from DBBase import DBBase
from webapp.db.Log import Logger
from utils.DBUtil import DBConn

class DBAuthority(DBBase):
	"""
	用户权限管理
	"""
	pass

	@classmethod
	def checkUrl(self, url):
		'''
		测试url是否在权限管理之内
		'''
		# Logger.info('DBAuthority.checkUrl begin')
		sql = 'select count(*) from mgame_tool.menu where url=%s'
		db = DBConn()
		rownum, db_res = db.query(sql, (url))
		rownum += 0
		for row in db_res:
			if row[0] >= 1:
				return True
				# Logger.info('DBAuthority.checkUrl end')
			elif row[0] == 0:
				return False
				# Logger.info('DBAuthority.checkUrl end')
				'''
			elif row[0] > 1:
				msg = 'DBAuthority.checkUrl:有重复url[%s]' % url
				Logger.error(msg)
				raise Exception(msg);
				'''
		msg = 'DBUserInfo.login:有重复url[%s]' % url
		Logger.error(msg)
		raise Exception(msg);
		# Logger.info('DBAuthority.checkUrl end')


	@classmethod
	def checkUserUrl(self, userName, url):
		'''
		验证用户是否有权限访问页面
		'''
		sql = '''
		select count(*) from mgame_tool.menu
		inner join mgame_tool.authority on menu.menu_id=authority.menu_id
		inner join mgame_tool.user_authority on user_authority.authority_id=authority.authority_id
		where user_authority.user_name=%s and menu.url=%s
		'''
		db = DBConn()
		rownum, db_res = db.query(sql, (userName, url))
		rownum += 0
		for row in db_res:
			if row[0] >= 1:
				return True
		return False
	
		
	@classmethod
	def selectMenu(self, userName, parnetId=0):
		'''
		查询用户权限
		return 返回用户可以访问的菜单列表
		'''
		returnValue = []
		sql = '''
		select menu.menu_id, menu.text, menu.url,menu.parent_id,menu.sort from mgame_tool.menu
		inner join mgame_tool.authority on menu.menu_id=authority.menu_id
		inner join mgame_tool.user_authority on user_authority.authority_id=authority.authority_id
		where user_authority.user_name=%s 
		order by menu.sort
		'''
		db = DBConn()
		rownum, db_res = db.query(sql, (userName))
		rownum += 0
		for row in db_res:
			menu = {}
			menu["id"] = row[0]
			menu["text"] = row[1]
			menu["url"] = row[2]
			menu["parentId"] = row[3]
			menu["sort"] = row[4]
			returnValue.append(menu)
		return returnValue


	@classmethod
	def selectAuthority(self, text):
		'''
		查找指定的用户
		'''
		Logger.info('DBAuthority.selectAuthority begin')
		returnValue = {}
		sql = ''' select authority_id,comment from mgame_tool.authority where comment=%s group by authority_id,comment '''
		db = DBConn()
		rownum, db_res = db.query(sql, (text))
		for row in 	db_res:
			temp = {}
			temp['id'] = row[0]
			temp['comment'] = row[1]
			returnValue.append(temp)
		if rownum == 0:
			return None
		else:
			return returnValue;


	@classmethod
	def selectAllAuthority(self, text=''):
		'''
		查询用户
		'''
		Logger.info('DBAuthority.selectAllAuthority begin')
		returnValue = []
		sql = ''' select authority_id,comment from mgame_tool.authority '''
		where = ''' where comment like %s '''
		groupBy = ''' group by authority_id,comment '''
		rownum, db_res = None, None
		db = DBConn()
		if text == '':
			rownum, db_res = db.query(sql + groupBy)
		else:
			sql = sql + where + groupBy
			rownum, db_res = db.query(sql, ('%' + text + '%'))
		rownum += 0
		for row in 	db_res:
			temp = {}
			temp['id'] = row[0]
			temp['comment'] = row[1]
			returnValue.append(temp)
		return returnValue;


	@classmethod
	def selectAuthorityById(self, id):
		'''
		通过id查找权限
		'''
		returnValue = []
		sql = ''' select authority_id,menu_id,comment from mgame_tool.authority where authority_id=%s '''
		db = DBConn()
		rownum, db_res = db.query(sql, (id))
		for row in 	db_res:
			temp = {}
			temp['authorityId'] = row[0]
			temp['menuId'] = row[1]
			temp['comment'] = row[2]
			returnValue.append(temp)
		return returnValue;
	
	
	@classmethod
	def selectAuthorityByUserName(self, userName):
		'''
		'''
		returnValue = []
		sql = ''' select user_name,authority_id from mgame_tool.user_authority where user_name=%s '''
		db = DBConn()
		rownum, db_res = db.query(sql, (userName))
		for row in 	db_res:
			returnValue = {}
			returnValue['userName'] = row[0]
			returnValue['authorityId'] = row[1]
			return returnValue
		return returnValue;
	
	
	@classmethod
	def insrtaaaaaaaaaaaaaaaa(self, text, menuIdList=None):
		sql = ''' insert into mgame_tool.authority(menu_id,comment) values(%s,%s)'''
		db = DBConn()
		param = []
		if menuIdList == None:
			param.append((-1, text))
		else:
			for menuId in menuIdList:
				param.append((menuId, text))
		rownum, db_res = db.execMany(sql, param)
		return rownum
		
	
	@classmethod
	def insrt(self, text, authorityId=None, menuIdList=None):
		sql = ''' insert into mgame_tool.authority(menu_id,comment) values(%s,%s)'''
		db = DBConn()
		param = []
		if menuIdList == None:
			rownum, db_res = db.query(sql, (-1, text))
			return db.getLastInsertId()
		else:
			sql = ''' insert into mgame_tool.authority(authority_id,menu_id,comment) values(%s,%s,%s)'''
			for menuId in menuIdList:
				rownum, db_res = db.query(sql, (authorityId, menuId, text))
		return rownum
	
		
	@classmethod
	def deleteByAuthorityId(self, authorityId):
		sql = ''' delete from mgame_tool.authority where authority_id=%s '''
		db = DBConn()
		rownum, db_res = db.query(sql, (authorityId))
		return rownum
	
	
	@classmethod
	def update(self, userName, authorityId):
		# sql = ''' replace mgame_tool.user_authority set authority_id=%s where user_name=%s '''
		sql = ''' replace into mgame_tool.user_authority(user_name,authority_id) values(%s,%s) '''
		db = DBConn()
		rownum, db_res = db.query(sql, (userName, authorityId))
		return rownum
