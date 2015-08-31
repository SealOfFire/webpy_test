# encoding:utf-8
import web;
from webapp.Log import Logger
from webapp.logic.AuthorityManagement import AuthorityManagement
from webapp.logic.MenuManagement import MenuManagement


class Common():
	"""
	页面处理基类
	"""


	@classmethod
	def init(self):
		"""
		初始化设置
		"""
		Common.initFinish = False;
		Logger.info('初始化网站 begin')
		web.config.debug = True;
		Common.urls = (
					 '/', 								'webapp.pages.Index.Index'  # 首页
					, '/error', 						'webapp.pages.Error.Error'  # 错误页面
					, '/login', 						'webapp.pages.Login.Login'  # 登录界面
					, '/userInfo/list', 				'webapp.pages.userInfo.List.List'  # 用户一览
					, '/userInfo/modify', 		'webapp.pages.userInfo.Modify.Modify'  # 用户信息编辑
					, '/userInfo/authority', 	'webapp.pages.userInfo.Authority.Authority'  # 用户权限
					, '/authority/list', 			'webapp.pages.authority.List.List'  #
					, '/authority/modify', 		'webapp.pages.authority.Modify.Modify'  #
					, '/gm/mail', 					'webapp.pages.gm.Mail.Mail'  # gm发邮件
					, '/gm/card', 					'webapp.pages.gm.Card.Card'  # gm卡
					, '/gm/diamond', 			'webapp.pages.gm.Diamond.Diamond'  # gm钻石
					, '/gm/gold', 					'webapp.pages.gm.Gold.Gold'  # gm金币
					, '/gameData/userList', 	'webapp.pages.gameData.UserList.UserList'  # 游戏内玩家数据
					, '/gameData/userInfo', 	'webapp.pages.gameData.UserInfo.UserInfo'  # 游戏内玩家数据
					)
		Logger.info('初始化网站 end')


	@classmethod
	def run(self):
		"""
		启动网站
		"""
		# 初始化
		Common.init();
		
		# 创建web应用
		Logger.info('创建web应用')
		Common.app = web.application(Common.urls, globals())
		
		# 创建session
		Logger.info('创建session')
		Common.initSession(Common.app);
		Common.session.menu = MenuManagement();
		
		# 加载模板
		Logger.info('加载模板')
		Common.render = web.template.render('templates/', base='baseframe', globals={'context': Common.session})
		# 
		# 设置错误页面
		# Common.app.notfound = Common.notfound
		# Common.app.internalerror = Common.internalerror
		# 加载设置
		Logger.info('加载设置')
		# Common.app.add_processor(Common.error_precessor);
		Common.app.add_processor(web.loadhook(Common.session_hook));
		# Common.app.add_processor(web.loadhook(Common.session.menu.setSelectedMenu));
		Common.app.add_processor(web.loadhook(AuthorityManagement.checkAuthority))
		# Common.app.add_processor(web.unloadhook(AuthorityManagement.checkAuthority))
		
		Logger.debug('网站启动')
		Common.initFinish = True
		Common.app.run();


	@classmethod
	def initSession(self, app):
		"""
		初始化session
		"""
		# 设置session
		web.config.session_parameters['cookie_name'] = 'webpy_session_id'
		web.config.session_parameters['timeout'] = 500  # session过期时间(秒)
		
		# session格式
		dictSession = {
				'userInfo':None  # 登录系统的用户信息
				, 'menu':MenuManagement()
				, 'exception':Exception("没有错误")  # 异常信息
				}
		
		# 创建session
		if web.config.get('_session') is None:
			Common.session = web.session.Session(app, web.session.DiskStore('sessions'), dictSession)
		else:
			Common.session = web.config._session


	@classmethod
	def error_precessor(self, handler):
		try:
			return handler()
		except Exception as e:
			# do something reasonable to handle the exception
			# print e
			# Common.session.exception = e
			return web.seeother('/error')
			# raise e
		
		
	@classmethod
	def session_hook(self):
		Common.session.menu.setSelectedMenu()
		web.ctx.session = Common.session


	@classmethod
	def notfound(self):
		return web.notfound("Sorry, the page you were looking for was not found.")


	@classmethod
	def internalerror(self):
		return web.internalerror("Bad, bad server. No donut for you.")


		
