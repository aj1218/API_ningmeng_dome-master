"""
==========
Author:TT
Time:2021/3/9  11:45 上午
Project: API_ningmeng_dome
Company:自动化测试
==========
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

testdate = HandlerExcel(conf.excel, "add").read_all_datas()


@ddt
class TestAdd(unittest.TestCase):

    def setUp(self) -> None:
        self.excel = HandlerExcel(conf.excel, "add")
        self.db = HandleDB()

    @classmethod
    def setUpClass(cls) -> None:
        mylog.info("***************** 加标接口   开始测试***************")
        # 清理EnvData属性
        clear_EnvData_attrs()

    @classmethod
    def tearDownClass(cls) -> None:
        mylog.info("***************** 加标接口   结束测试***************")

    @data(*testdate)
    def test_add(self, case):
        # 替换请求数据 case
        case = replace_case_by_regular(case)
        # 前置sql - 查询 在替换
        # 发送请求，是否都有token
        if hasattr(EnvData, "admin_token"):
            res = send_request(case["method"], case["url"], case["data"], token=EnvData.admin_token).json()
        else:
            res = send_request(case["method"], case["url"], case["data"]).json()

        # 如果有替换表达式，提取数据，设置为全部变量
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"], res)
        # 如果有期望结果 则断言
        # 断言
        try:
            if case["expected"]:
                # 将期望结果转成字典对象 再去比对
                expected_data = json.loads(case["expected"])
                self.assertEqual(expected_data["msg"], res["msg"])
                self.assertEqual(expected_data["code"], res["code"])
            # 如果有check_sql 则数据库校验
            if case["check_sql"]:
                result = self.db.select_one_data(case["check_sql"])
                self.assertIsNotNone(result)
                mylog.info("数据库查询数据为：{}".format(result))
            self.excel.write_back(conf.excel, "add", case["case_id"] + 1, 11,
                                  json.dumps(res["code"], ensure_ascii=False))
        except AssertionError as e:
            mylog.info("断言失败！！！")
            mylog.exception(e)
            self.excel.write_back(conf.excel, "add", case["case_id"] + 1, 11,
                                  json.dumps(res["code"], ensure_ascii=False))
            raise e
