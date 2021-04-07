"""
==========
Author:TT
Time:2021/2/20  10:53 上午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
from configparser import ConfigParser

from common.Case_file import conf


#实例化
# conf = ConfigParser()
#
# #读取配置文件
# res=conf.read('py30.ini',encoding='utf-8')
# print(res)
#
# #读取配置文件的某一项配置值：get
# test=conf.get('log','name')
# print(test)
#
# # #获取当前section ini全部的类名
# # print(conf.sections())
#
# #拿到ini文件当中的属性名
# s = conf.options('log')
# print(s)
#
# #写入数据
# conf.set('log','file_name','py30303030.log')
# conf.write(open('py30.ini','w',encoding='UTF-8'))
#
class HandlerConfig(ConfigParser):

    def __init__(self,file_name):
        super().__init__()
        self.read(file_name,encoding="UTF-8")



con = HandlerConfig(conf.Ini_file)
if __name__ == '__main__':
    print(con.get('general_user','user'))