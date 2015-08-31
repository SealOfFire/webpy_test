# encoding:utf-8
from DBBase import DBBase
from webapp.db.Log import Logger
from utils.DBUtil import DBConn

class DBMenu(DBBase):
	
	
	@classmethod
	def selectAll(self):
		'''
		
		'''
		returnValue = []
		Logger.info('DBMenu.selectAll begin')
		db = DBConn()
		sql = 'select menu_id,text,url,sort from mgame_tool.menu where parent_id>0 order by parent_id,sort'
		rownum, db_res = db.query(sql)
		rownum += 0
		for row in	 db_res:
			temp = {}
			temp['menuId'] = row[0]
			temp['text'] = row[1]
			temp['url'] = row[2]
			temp['sort'] = row[3]
			returnValue.append(temp)
		return returnValue


	@classmethod
	def selectByMenuId(self, menuId):
		'''
		'''
		returnValue = {}
		sql = ''' select  menu_id,text,url,sort from mgame_tool.menu where menu_id=%s '''
		db = DBConn()
		rownum, db_res = db.query(sql, (menuId))
		rownum += 0
		for row in	 db_res:
			returnValue['menuId'] = row[0]
			returnValue['text'] = row[1]
			returnValue['url'] = row[2]
			returnValue['sort'] = row[3]
		return returnValue
