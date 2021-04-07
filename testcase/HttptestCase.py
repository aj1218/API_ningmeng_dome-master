"""
==========
Author:TT
Time:2021/2/5  3:42 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
import os
import unittest
import ddt
from testcase.headler import Headler
from testcase.Do_excel import HandlerExcel
from testcase.logs import Mylog
mylog = Mylog(name="py30",file='my_logs.log')
# test_data = [
#     {"username":"python30","pwd":"11111","code":{"msg":"登陆成功"}},
#     {"username": "", "pwd": "11111", "code": {"msg": "登陆成功"}},
#     {"username": "python30", "pwd": "", "code": {"msg": "登陆成功"}},
#     {"username": "python", "pwd": "11111", "code": {"msg": "登陆成功"}},
#     {"username": "python30", "pwd": "11111122", "code": {"msg": "登陆成功"}},
#     {"username": "", "pwd": "", "code": {"msg": "登陆成功"}},
#     {"username": "python30", "pwd": "11111", "code": {"msg": "登陆成功11"}}
#
# ]
file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"Excel.xlsx")
test_data = HandlerExcel(file_dir,'login').read_all_datas()
@ddt.ddt()
class TestCode(unittest.TestCase):
    @ddt.data(*test_data)
    def test_login(self,data):
        mylog.info("***********开始测试啦******************")
        mylog.info("测试数据为：{}".format(data))
        res = Headler().testHeadler(data["username"],data["pwd"])
        # mylog.info("测试结果为：{}".format(res))
        try:
            self.assertEqual(res,data["check"])
        except AttributeError as e:
            mylog.exception("断言失败，用例不通过")
            raise e
        else:
            mylog.exception("断言通过，用例通过")
        mylog.exception("**********用例执行结束****************")

