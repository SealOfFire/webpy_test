# encoding:utf-8
import web
from webapp.Log import Logger
from webapp.Common import Common
from webapp.pages.BasePage import BasePage
from webapp.logic.AuthorityManagement import AuthorityManagement
from webapp.logic.MenuManagement import MenuManagement


class Modify(BasePage):
	"""
	用户信息编辑
	"""
	
	id = -1
	menuAuthority = []
	dictMenuAuthority = {}
	menuAll = [];
	text = ""
	selectMenuId = []
	
	def GET(self):
		'''
		'''
		urlParam = web.input(id=None)
		self.id = urlParam.id
		'''
		self.menuAll = MenuManagement.selectAll()
		for item in self.menuAll:
			self.dictMenuAuthority[item['menuId']] = ""
		'''
		if self.id == None:
			self.id = ""
			self.menuAll = []
			self.text = ""
		else:
			self.menuAuthority = AuthorityManagement.selectAuthorityById(self.id)
			self.text = self.menuAuthority[0]["comment"]
			self.menuAll = MenuManagement.selectAll()
			for item in self.menuAll:
				self.dictMenuAuthority[item['menuId']] = ""
				
			for item in self.menuAuthority:
				self.dictMenuAuthority[item['menuId']] = 'checked'
		
		return Common.render.authority.modify(self)
	
	
	def POST(self):
		'''
		'''
		self.id = web.input().authorityId
		self.temp = web.input(menuId4=False).menuId4
		self.selectMenuId = [];
		self.text = web.input().text
		self.menuAll = MenuManagement.selectAll()
		for item in self.menuAll:
			temp = None
			exec('temp=web.input(menuId%d=False).menuId%d' % (item["menuId"], item["menuId"]))
			if temp == "on":
				self.selectMenuId.append(item["menuId"])

		if self.id == "":
			# 新建数据
			Logger.info('新建数据')
			self.id = AuthorityManagement.createAuthority(self.text)

			'''
			for item in self.menuAll:
				self.dictMenuAuthority[item['menuId']] = ""
			'''
			
		else:
			# 更新数据
			Logger.info('更新数据')
			
			AuthorityManagement.updateAuthority(self.id, self.text, self.selectMenuId)
			
		# return Common.render.authority.modify(self)
		return web.seeother('/authority/modify?id=' + str(self.id))
	
	def checkForm(self):
		
		return True
		
		
