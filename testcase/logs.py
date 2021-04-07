"""
==========
Author:TT
Time:2021/2/18  6:51 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""

  #日志名字
  #1：日志级别(Level)：DEBUG WANGING CRITICAL
  #2：输出渠道(handle)：文件 控制台
  #3：日志内容（Format） 时间-哪个文件-哪行代码-输出内容
#logging模块 默认的root日志收集器 默认的输出级别WARNING
#第一步： 创建一个日志收集器 logging.getLogging("收集器的名字")
#第二步：给日志收集器，设置日志级别 ：logger.setLevel(logging.INFO)
#第三步：给日志收集器 创建一个输出渠道 handle = logging.StreamHandler()
#第四步： 给渠道设置一个输出内容的格式
# 第五部：将设置的格式，绑定到渠道中，将日志格式于渠道关联起来
# 第六步：将设置好的渠道添加到日志收集器上
# import logging

# logger=logging.getLogger("py30") #创建一个日志收集器
# #设置日志输出级别
# logger.setLevel(logging.INFO)
# #设置日志输出在哪个渠道
# handle= logging.StreamHandler()
# #设置渠道的内容输出格式
# fmt = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
# forrmat=logging.Formatter(fmt)
#
# #将日志格式绑定到渠道中
# handle.setFormatter(forrmat)
#
# # 将设置好的渠道添加到日志收集器上
# logger.addHandler(handle)
#
# #添加fileHandler
# handler1=logging.FileHandler("my_logs.log",encoding='UTF-8')
# handler1.setFormatter(forrmat)
# logger.addHandler(handler1)
# logger.info("qwert234567890-j")
# logger.info("qwertj")
#

import logging
from testcase.ConfigParse import conf

class Mylog(logging.Logger):
    def __init__(self,file=None):
        #设置输出级别，设置输出渠道，设置输出日志格式
        super().__init__(conf.get('log','name'),conf.get('log','level'))
        fmt = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        forrmat=logging.Formatter(fmt)

        #控制渠道
        handle= logging.StreamHandler()
        handle.setFormatter(forrmat)
        self.addHandler(handle)

        if file:
            #文件渠道
            handle1 = logging.FileHandler(file,encoding='UTF-8')
            handle1.setFormatter(forrmat)
            self.addHandler(handle1)

if conf.get('log','file_ok'):
    file = conf.get('log','file_name')
else:
    file = None


mylog = Mylog(file)
if __name__ == '__main__':
    mylog.info("qwerghjkasdfgjgfdsa12345678iop")




















