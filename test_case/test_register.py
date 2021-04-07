"""
==========
Author:TT
Time:2021/2/23  6:16 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
import json
import unittest
from ddt import ddt,data
from requestHttp.Request_Package import send_request
from Do_excel.DoExcel import HandlerExcel
from common.Case_file import conf
from Outputs.logs.logs import mylog
from common.PyMysql import HandleDB
from common.handle_phone import get_new_phone
from common.handler_data import replace_lable
from Outputs.Ini.ConfigParseCase import con
he = HandlerExcel(conf.excel,"register").read_all_datas()

# for item in he:
#     print(item)

@ddt
class TestRegister(unittest.TestCase):
    def setUp(self) -> None:
        self.db=HandleDB()
        self.excel = HandlerExcel(conf.excel,"register")

    @classmethod
    def setUpClass(cls) -> None:
        mylog.info("========注册模块 开始执行==========")

    @classmethod
    def tearDownClass(cls) -> None:
        mylog.info("========注册模块 执行结束==========")


    @data(*he)
    def test_register_ok(self,data):
        """
        #步骤：测试数据 - 发起请求
        #断言
        :return:
        """
        mylog.info("执行用例{}----{}".format(data["case_id"],data["case_name"]))
        #替换 - 动态--请求数据重的#phone#替换为new_phone
        #sql 语句也需要替换  check_sql里的#phone# 替换new_phone
        #find=-1就是没有找到这个数据  find！=-1 就是找到了这个数据
        if data["data"].find("#phone#")!=-1:
            new_phone = get_new_phone()
            data=replace_lable(data,"#phone#",new_phone)
            # data["data"]=data["data"].replace("#phone#",new_phone)
            # data["check_sql"] = data["check_sql"].replace("#phone#", new_phone)

        # 将check的字符串转换为字典对象
        data["data"] = json.loads(data["data"])
        expected = eval(data["expected"])
        res = send_request(data["method"],data["url"], data["data"]).json()
        print(res)
        mylog.info("本用例的期望结果是：{}".format(data["expected"]))
        #如果check_sql有值，说明要做数据库校验


        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            if data["check_sql"]:
                result = self.db.select_one_data(data["check_sql"])
                self.assertIsNotNone(result)
                mylog.info("数据库查询数据为：{}".format(result))
            self.excel.write_back(conf.excel, "register", data["case_id"] + 1, 9, json.dumps(res["msg"],ensure_ascii=False))

        except AssertionError as e:
            mylog.info("断言失败！！！")
            mylog.exception(e)
            self.excel.write_back(conf.excel, "register", data["case_id"] + 1, 9, json.dumps(res["msg"], ensure_ascii=False))
            raise e



