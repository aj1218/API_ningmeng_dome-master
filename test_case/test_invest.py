"""
==========
Author:TT
Time:2021/3/4  6:51 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
1.项目 有一个项目 且项目为竞标状态
    两个接口：创建项目，审核项目。借钱：1000万

2。普通用户。有一个用户且用户余额：10万
    两个接口：登陆，充值2000快

"""
import json
import unittest
from ddt import ddt, data

from Do_excel.DoExcel import HandlerExcel
from Outputs.logs.logs import mylog
from common.Case_file import conf
from common.handler_data import EnvData, replace_case_by_regular, clear_EnvData_attrs
from common.handler_extract_data_from_response import extract_data_from_response
from requestHttp.Request_Package import send_request
from common.PyMysql import HandleDB

test_data = HandlerExcel(conf.excel, "invert").read_all_datas()
# print(test_data)

@ddt
class InvestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.excel = HandlerExcel(conf.excel, "add")
        self.db = HandleDB()

    @classmethod
    def setUpClass(cls) -> None:
        mylog.info("***************** 投资接口   开始测试***************")
        clear_EnvData_attrs()

    @classmethod
    def tearDownClass(cls) -> None:
        mylog.info("***************** 投资接口   结束测试***************")



    @data(*test_data)
    def test_invest(self,case):
        #替
        case = replace_case_by_regular(case)
        # 前置sql - 查询 在替换
        # 发送请求，是否都有token
        if hasattr(EnvData,"admin_token"):
            res = send_request(case["method"], case["url"], case["data"], token=EnvData.admin_token).json()
        else:
            res = send_request(case["method"], case["url"], case["data"]).json()
        # 如果有替换表达式，提取数据，设置为全部变量
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"], res)


if __name__ == '__main__':
    unittest.main()




