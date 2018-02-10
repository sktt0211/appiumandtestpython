# _*_ coding: utf-8 _*_
import logging
import os.path
import time

class loogger():
    def __init__(self,logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件

        # time.strftime()
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 两个参数一个是 格式，另一个是 显示的时间
        print ("time.localtime() : %s" % time.localtime())
        print(time.localtime())
        print(rq)

        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'

         # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录

        log_name = log_path + rq + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)



    def getlog(self):
        return self.logger