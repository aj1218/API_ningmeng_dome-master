"""
==========
Author:TT
Time:2021/3/5  2:44 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
从响应结果当中提取响应的值

注册 用户名和密码
登陆 同一用户名和密码
充值 上一个接口返回值里面的 token - member_id
提现 登陆接口返回值里面的 token - member_id
加标
"""
import unittest
from ddt import ddt, data

from Do_excel.DoExcel import HandlerExcel
from common.Case_file import conf
from common.handle_phone import get_new_phone
from common.handler_data import EnvData, replace_case_by_regular, clear_EnvData_attrs
from common.handler_extract_data_from_response import extract_data_from_response
from requestHttp.Request_Package import send_request

testdate = HandlerExcel(conf.excel, "business").read_all_datas()


@ddt
class TestUserBusiness(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        clear_EnvData_attrs()
        # 生成一个新的手机号码 设置成为一个环境变量
        new_phone = get_new_phone()
        setattr(EnvData, "phone", new_phone)  # 都是字符串

    @data(*testdate)
    def test_user_business(self, case):
        """
        1。替换数据

        2。发起请求
        3。有要提取数据的 并设置为全局变量
        :return:
        """
        # 1。替换数据
        replace_case_by_regular(case)
        # 2。发起请求,判断是否需要token

        if hasattr(EnvData, "token"):
            res = send_request(case["method"], case["url"], case["data"], token=EnvData.token).json()
        else:
            res = send_request(case["method"], case["url"], case["data"]).json()

        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],res)


