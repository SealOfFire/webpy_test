# encoding:utf-8
import web
from utils.DBUtil import DBConn
from webapp.logic.Log import Logger
from webapp.logic.UserInfo import UserInfo
from webapp.db.DBUserInfo import DBUserInfo
from webapp.db.DBAuthority import DBAuthority

class AuthorityManagement:
	"""
	权限处理
	"""
	
	@classmethod
	def login(self, userName, password):
		"""
		用户登录
		returns:
			true:登录成功
			false:登录失败
		"""
		
		if DBUserInfo.login(userName, password):
			Logger.info("用户验证成功")
			userInfo = UserInfo(userName, 0);
			from webapp.Common import Common
			Common.session.userInfo = userInfo
			# 初始化菜单数据
			from MenuManagement import MenuManagement
			Common.session.menu = MenuManagement(userName)
			return True
		else:
			Logger.info("用户验证失败")
			return False;
	
	
	@classmethod
	def checkAuthority(self):
		"""
		验证用户权限
		"""
		Logger.info('AuthorityManagement.checkAuthority begin');
		
		# 判断当前浏览的页面是否需要登陆
		exception = None
		if DBAuthority.checkUrl(web.ctx.path):
			Logger.info("访问的路径[%s]是受权限保护路径" % str(web.ctx.path))
			# 判断用户权限是否可以浏览页面
			
			# 判断用户登录
			from webapp.Common import Common
			if Common.session.userInfo == None:
				exception = Exception(u"用户没有登录")
			else:
				userInfo = Common.session.userInfo
				# 判断浏览权限
				if DBAuthority.checkUserUrl(userInfo.userName, str(web.ctx.path)):
					pass;
				else:
					exception = Exception(u"没有权限浏览网页")
					
		else:
			Logger.info("访问的路径[%s]" % str(web.ctx.path))
		
		if exception == None:
			return
		else:
			Common.session.exception = exception;
			raise exception
		
		Logger.info('AuthorityManagement.checkAuthority end');


	@classmethod
	def selectAll(self, text):
		'''
		查找用户
		'''
		value = DBAuthority.selectAllAuthority(text)
		return value
	
	
	@classmethod
	def select(self, text):
		'''
		查找指定用户
		'''
		value = DBAuthority.selectAuthority(text)
		return value
	
	
	@classmethod
	def selectAuthorityById(self, id):
		# 权限信息
		value = DBAuthority.selectAuthorityById(id)
		return value
	
	@classmethod
	def selectAuthorityByUserName(self, userName):
		# 权限信息
		value = DBAuthority.selectAuthorityByUserName(userName)
		return value
	
	@classmethod
	def createAuthority(self, text):
		value = DBAuthority.insrt(text)
		return value
	
	
	@classmethod
	def replaceAuthority(self, userName, authorityId):
		value = DBAuthority.update(userName, authorityId)
		return value
	
	
	@classmethod
	def updateAuthority(self, authorityId, text, menuIdList):
		DBConn().begin();
		try:
			DBAuthority.deleteByAuthorityId(authorityId)
			DBAuthority.insrt(text, authorityId, menuIdList)
			DBConn().commit(); 
		except Exception, e:
			print e
			DBConn().rollback();
