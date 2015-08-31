# encoding:utf-8
import web
from webapp.logic.Log import Logger
from webapp.db.DBAuthority import DBAuthority
from webapp.db.DBMenu import DBMenu

	
class MenuManagement:
	"""
	菜单项目管理
	"""
	
	# 菜单列表
	menuList = [];
	
	# 选中的菜单项目
	selectedMainMenu = 1;
	
	# 选中的子菜单项目
	selectedSubMenu = 2;
	
	
	def __init__(self, userName=None):
		if userName == None:
			# 默认菜单
			pass
		else:
			# 初始化用户菜单
			self.initMenu(userName)


	def __str__(self):
		text = ''
		for menu in self.menuList:
			text += u'id:[%s] text:[%s] url:[%s] \r\n' % (menu['id'], menu['text'], menu['url'])
			for subMenu in menu['subMenu']:
				text += u'		id:[%s] text:[%s] url:[%s] \r\n' % (subMenu['id'], subMenu['text'], subMenu['url'])
		return text


	def initMenu(self, userName):
		"""
		初始化菜单项目
		"""
		Logger.info('MenuManagement.initMenu begin');
		self.menuList = []
		# 获取所有菜单项目
		menu = DBAuthority.selectMenu(userName)
		for subMenu in menu:
			# 查找子菜单所属的主菜单
			flg=True
			for menu in self.menuList:
				if subMenu["parentId"] == menu["id"]:
					menu["subMenu"].append(subMenu)
					flg=False;
			
			if flg:
				# 创建主菜单
				temp = DBMenu.selectByMenuId(subMenu["parentId"])
				menu = {}
				menu['id'] = temp['menuId']
				menu['text'] = temp['text']
				menu['url'] = temp['url']
				menu['sort'] = temp['sort']
				menu["subMenu"] = []
				menu["subMenu"].append(subMenu)
				self.menuList.append(menu)
				
		self.menuList.sort(key=self.sort)
		# sorted(self.menuList,key=sort)
		
		'''
		# 获取一级菜单项目
		menu = DBAuthority.selectMenu(userName, 0)
		for item in menu:
			subMenu = DBAuthority.selectMenu(userName, item["id"])
			menuItem = {};
			menuItem["id"] = item["id"]
			menuItem["text"] = item["text"]
			menuItem["url"] = item["url"]
			menuItem["subMenu"] = subMenu
			self.menuList.append(menuItem)
		'''
		# 整理菜单项目
		for item in self.menuList:
			item['url'] = item['subMenu'][0]['url']
		Logger.info('MenuManagement.initMenu end');
	
	def sort(self,menu):
		return menu['sort']
	
	def setSelectedMenu(self):
		'''
		当前选中的菜单项目
		'''
		Logger.info('MenuManagement.setSelectedMenu begin');
		# print web.ctx.path
		# 根据请求路径查看改路径的主菜单和子菜单项目
		for mainMenu in self.menuList:
			if mainMenu.has_key('url'):
				if mainMenu['url'] == web.ctx.path:
					self.selectedMainMenu = mainMenu['id']
					self.selectedSubMenu = mainMenu['id']
					Logger.debug("选中的主菜单项目是[%d:%s]" % (mainMenu['id'], mainMenu['text']))
					Logger.debug("选中的子菜单项目是[%d:%s]" % (mainMenu['id'], mainMenu['text']))
					break;
			else:
				for subMenu in mainMenu["subMenu"]:
					if subMenu['url'] == web.ctx.path:
						self.selectedMainMenu = mainMenu['id']
						self.selectedSubMenu = subMenu['id']
						Logger.debug("选中的主菜单项目是[%d:%s]" % (mainMenu['id'], mainMenu['text']))
						Logger.debug("选中的子菜单项目是[%d:%s]" % (mainMenu['id'], mainMenu['text']))
						break;
		Logger.info('MenuManagement.setSelectedMenu end');
	
	
	@classmethod
	def selectAll(self):
		'''
		查询所有菜单项目
		'''
		value = DBMenu.selectAll()
		return value
	
	
	def renderHtmlMenu(self):
		"""
		生成菜单项目
		"""
		li = ""
		for mainMenu in self.menuList:
			li += "<li><a id='%s' href='%s'>%s</a></li>" % (mainMenu['id'], mainMenu['url'], mainMenu['text'])
		return "<ul>" + li + "</ul>"


	def renderHtmlSubMenu(self):
		"""
		生成子菜单项目
		"""
		li = ""
		for menu in self.menuList:
			if self.selectedMainMenu == menu["id"]:
				for subMenu in menu["subMenu"]:
					li += "<li><a id='%s' href='%s'>%s</a></li>" % (subMenu['id'], subMenu['url'], subMenu['text'])
				return  "<ul>" + li + "</ul>"
