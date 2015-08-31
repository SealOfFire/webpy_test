# encoding:utf-8
import web
import logging  
import logging.handlers  
'''
fmt = '[%(asctime)s] - [%(levelname)s] - [%(name)s] - %(message)s'
logging.basicConfig(level=logging.NOTSET, format=fmt)
# logging.basicConfig()


# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(logging.Formatter(fmt))
# logging.getLogger('').addHandler(console)


filehandler = logging.handlers.TimedRotatingFileHandler('webapp_', when="M", interval=1, backupCount=0, encoding=None, delay=False, utc=False)
filehandler.suffix = "%Y%m%d.log"
filehandler.setFormatter(logging.Formatter(fmt))
logging.getLogger('').addHandler(filehandler)
'''
# logger = logging.getLogger('web');
# logger.debug("日志初始化完成")
'''
logger1 = logging.getLogger('myapp.area1')  
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')  
logger1.info('How quickly daft jumping zebras vex.')  
logger2.warning('Jail zesty vixen who grabbed pay from quack.')  
logger2.error('The five boxing wizards jump quickly.')
'''


class Logger():
	"""
	日志处理
	"""
	fileName = "webapp.log"
	fmt = '[%(asctime)s] - [%(levelname)s] - [%(name)s] - %(message)s'
	logging.basicConfig(level=logging.NOTSET, format=fmt)

	filehandler = logging.handlers.TimedRotatingFileHandler(fileName, when="M", interval=1, backupCount=0, encoding=None, delay=False, utc=False)
	filehandler.suffix = "%Y%m%d.log"
	filehandler.setFormatter(logging.Formatter(fmt))
	logging.getLogger('').addHandler(filehandler)

	logger = logging.getLogger('web');
	logger.debug("日志初始化完成")
	
	'''
	@classmethod
	def __init__(self):
		logger = logging.getLogger('web');
		logger.debug("日志初始化完成")
	'''
	
	@classmethod
	def msg(self, msg):
		userName = 'anonymous'
		from  webapp.Common import Common
		if Common.initFinish:
			if Common.session.userInfo == None:
				userName = str(web.ctx.ip)
			else:
				userName = str(Common.session.userInfo.userName)
		# print userName, msg
		return "[%s] - %s" % (userName, msg)
	
	
	@classmethod
	def info(self, msg):
		self.logger.info(Logger.msg(msg))
		
	@classmethod
	def debug(self, msg):
		self.logger.debug(Logger.msg(msg))
		
		
	@classmethod
	def critical(self, msg):
		self.logger.critical(Logger.msg(msg))
	
	@classmethod
	def error(self, msg):
		self.logger.error(Logger.msg(msg))
		
	@classmethod
	def warning(self, msg):
		self.logger.warning(Logger.msg(msg))
		
