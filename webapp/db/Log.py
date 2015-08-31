# encoding:utf-8
import logging  
import logging.handlers  
from webapp.Log import Logger
# import webapp.Log
# logger = Log.logging.getLogger('logic');

class Logger(Logger):
	'''
	'''
	logger = logging.getLogger('logic');
	logger.debug("数据库处理日志初始化完成")