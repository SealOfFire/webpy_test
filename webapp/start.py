# encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from webapp.Common import Common
from utils.DBUtil import *


if __name__ == "__main__":
	comm = Common();
	DBConn.initConnPoll(3)
	comm.run()

