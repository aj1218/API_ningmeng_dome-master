"""
==========
Author:TT
Time:2021/3/1  11:19 上午
Project: API_ningmeng_dome
Company:自动化测试
==========
充值接口
    前置：登陆
    拿到2个数据 id token
    把前置数据传递给到用例
充值接口的请求数据：id
        请求头：token
"""
import json

from jsonpath import jsonpath
import unittest
from ddt import ddt, data

from common.handle_phone import get_old_phone
from requestHttp.Request_Package import send_request
from Do_excel.DoExcel import HandlerExcel
from common.Case_file import conf
from common.PyMysql import HandleDB
from common.handler_data import replace_lable, EnvData, replace_case_by_regular,clear_EnvData_attrs
from Outputs.logs.logs import mylog

he = HandlerExcel(conf.excel, "recharge").read_all_datas()
db = HandleDB()


@ddt
class TestRecharge(unittest.TestCase):
    def setUp(self) -> None:
        self.excel = HandlerExcel(conf.excel, "recharge")

    def tearDown(self) -> None:  # 每条用例执行之后就删除一下上一条用例的数据
        if hasattr(EnvData, "money"):
            delattr(EnvData, "money")

    @classmethod
    def setUpClass(cls) -> None:
        """
        登陆接口调用
        得到的id token 设置为类属性
        :return:
        """
        # 清理 EnvData 里面设置的属性
        clear_EnvData_attrs()
        mylog.info("========充值模块 开始执行==========")
        # 得到用户名和密码
        user, password = get_old_phone()
        # 登陆接口调用
        data = {"mobile_phone": user, "pwd": password}
        res = send_request("POST", "/member/login", data)
        print(res)
        setattr(EnvData, "member_id", str(jsonpath(res.json(), "$..id")[0]))
        setattr(EnvData, "token", jsonpath(res.json(), "$..token")[0])
        cls.token = jsonpath(res.json(), "$..token")[0]
        cls.member_id = jsonpath(res.json(), "$..id")[0]

    @classmethod
    def tearDownClass(cls) -> None:

        mylog.info("========充值模块 执行结束==========")

    @data(*he)
    def test_recharge(self, data):
        mylog.info("执行用例{}----{}".format(data["case_id"], data["case_name"]))
        # 数据库--查询当前用户的余额
        # if data["data"].find("#member_id#") != -1:
        #     replace_lable(data, "#member_id#", str(self.member_id))
        #     mylog.info("用户的menber_id：{}".format(self.member_id))
        data = replace_case_by_regular(data)
        print(type(data))
        mylog.info("用户的menber_id：{}".format(EnvData.member_id))

        # 数据库--查询当前用户的余额
        print(data["check_sql"])
        if data["check_sql"]:
            uesr_money_before = db.select_one_data(data["check_sql"])["amount"]
            mylog.info("用户充值之前的余额：{}".format(uesr_money_before))
            # 得到期望的用户余额，充值之前的余额+充值的钱
            recharge_money = json.loads(data["data"])["amount"]
            mylog.info("用户充值的金额：{}".format(recharge_money))
            expected_user_leave_amount = round(float(uesr_money_before) + float(recharge_money), 2)
            # data = replace_lable(data, "#money#", str(expected_user_leave_amount))
            setattr(EnvData, "money", str(expected_user_leave_amount))
            data = replace_case_by_regular(data)
            mylog.info("用户充值之后的金额：{}".format(expected_user_leave_amount))

        # 发送请求 -- 给用户充值
        # 充值接口调用
        res = send_request(data["method"], data["url"], data["data"], token=EnvData.token).json()
        mylog.info("用户充值之前的返回数据：{}".format(res))
        self.excel.write_back(conf.excel, "recharge", data["case_id"] + 1, 10,
                              json.dumps(res["msg"], ensure_ascii=False))
        # 将期望结果转成字典对象 再去比对
        expected_data = json.loads(data["expected"])
        # 断言
        try:
            self.assertEqual(expected_data["msg"], res["msg"])
            self.assertEqual(expected_data["code"], res["code"])
            if data["check_sql"]:
                self.assertEqual(str(res["data"]["id"]), expected_data["data"]["id"])
                self.assertEqual(res["data"]["leave_amount"], expected_data["data"]["leave_amount"])
                # 数据库 - 查询当前用户的余额
                uesr_money_after = db.select_one_data(data["check_sql"])["amount"]
                mylog.info("用户充值之后的余额：{}".format(uesr_money_after))
                self.assertEqual("{:.2f}".format(expected_data["data"]["leave_amount"]),
                                 "{:.2f}".format(float(uesr_money_after)))
        except AssertionError as e:
            mylog.info("断言失败！！！")
            mylog.exception(e)
            self.excel.write_back(conf.excel, "recharge", data["case_id"] + 1, 10,
                                  json.dumps(res["msg"], ensure_ascii=False))
            raise e


if __name__ == '__main__':
    unittest.main()
