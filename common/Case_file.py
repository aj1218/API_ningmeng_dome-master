#coding:utf-8
"""
==========
Author:TT
Time:2021/2/24  6:03 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
import os
from datetime import datetime


class ConfigCase:
    #文件路径
    file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #excel文件路径
    excel = os.path.join(file_dir,"Case_file/testExcel.xlsx")
    print(excel)

    #case路径
    test_case = os.path.join(file_dir,"test_case")

    #html路径
    date = datetime.now().strftime("%Y-%m-%d%H%M")
    HTML = os.path.join(file_dir,"Outputs/report/{}".format(date)+"_report.html")

    #ini文件
    Ini_file = os.path.join(file_dir,"Outputs/Ini/py30.ini")

    #los文件路径
    log_file = os.path.join(file_dir,"Outputs/logs")


conf = ConfigCase()
print(conf.log_file)