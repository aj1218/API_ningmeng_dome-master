"""
==========
Author:TT
Time:2021/2/20  3:31 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
#
# import os
#
# class pathURL:
#
#     file_dir = os.path.dirname(os.path.abspath(__file__))
#     print(file_dir)
#
#     #ini文件
#     Ini =os.path.join(file_dir, 'py30.ini')
#     print(Ini)
#
#     # log文件
#     log = os.path.join(file_dir, 'logs.py')
#     print(log)
#
#     # Excel文件
#     excel = os.path.join(file_dir, 'Excel.xlsx')
#     print(excel)
#
# path = pathURL()

import json
data='[{"case_name": "负数", "modle_name": "充值", "url": "/member/recharge", "method": "post"}]'
data=json.dumps(data,ensure_ascii=False)
print(data)
print(type(data))