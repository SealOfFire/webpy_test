# encoding:utf-8
import web
from webapp.Common import Common
from webapp.pages.BasePage import BasePage
from webapp.logic.AuthorityManagement import AuthorityManagement

class Authority(BasePage):
	'''
	用户权限
	'''
	
	userName = ""
	authorityList = []
	authorityId = 0;
	
	def GET(self):
		'''
		'''
		urlParam = web.input(un=None)
		self.userName = urlParam.un
		self.authorityList = AuthorityManagement.selectAll("")
		self.authorityId = AuthorityManagement.selectAuthorityByUserName(self.userName)
		for item in self.authorityList:
			if self.authorityId !=[] and item['id'] == self.authorityId['authorityId']:
				item['checked'] = 'checked'
			else:
				item['checked'] = ''
		
		return Common.render.userInfo.authority(self)
	
	
	def POST(self):
		'''
		'''
		self.authorityId = web.input().rdoAuthroity
		self.userName = web.input().hidUserName
		AuthorityManagement.replaceAuthority(userName=self.userName, authorityId=self.authorityId)
		return web.seeother('/userInfo/authority?un=' + str(self.userName))
