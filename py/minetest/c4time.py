# _*_ coding: utf-8 _*_
import logging
import os.path
import time


rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# 两个参数一个是 格式，另一个是 显示的时间
#print("time.localtime() : %s" % time.localtime())
print(time.localtime())
print(rq)
#rint(rw)