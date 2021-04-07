"""
==========
Author:TT
Time:2021/2/4  6:24 下午
Project: API-TestCode
Company:自动化测试
==========
"""
"""
==========
Author:TT
Time:2021/2/26  5:15 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
一条用例当中，request， url ,check_data 需要进行替换


"""
import json
import re

from jsonpath import jsonpath

from Do_excel.DoExcel import HandlerExcel
from Outputs.Ini.ConfigParseCase import con
from common.Case_file import conf
from common.handle_phone import get_old_phone
from requestHttp.Request_Package import send_request
from Outputs.logs.logs import mylog

class EnvData:
    """
    存储用例要使用到的数据 动态设置
    """

def clear_EnvData_attrs():
    # 清理 EnvData 里面设置的属性
    values = dict(EnvData.__dict__.items())  # 这是一个可迭代对象
    print(values)
    for key, value in values.items():  # 转换成为字典之后，在点里面的items 进行遍历查找，取值
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)

def replace_case_by_regular(date):
    """
    对excel当中，读取出来的整条测试用例，做替换
    包括url method，monry等
    :param case: 得到的excel数据
    :return:
    """
    for key, value in date.items():
        # key不能为空，替换的动作只能是字符串，谁是谁的对象
        if date[key] is not None and isinstance(date[key], str):  # 确保是字符串
            date[key] = regular_expression(value)
    mylog.info("正则表达式替换之后的请求数据：\n{}".format(date))
    return date

    # 把case自典从excel中读取出来的一条用例数据 转换为字符串
    # case_str = json.dumps(case)
    # # 替换
    # new_case = regular_expression(case_str)
    # # 把替换的字符串转换成为字典
    # case_dict = json.loads(new_case)
    #
    # return case_dict
def regular_expression(testdata):
    """

    :param data: 将字符串中，匹配"#(.*?)#"部分，替换对应的真实数据，只从两个地方获取
    来自于：1，环境变量 （EnvData）2，配置文件
    :return:返回的是替换之后的字符串
    """
    # 通用
    res = re.findall("#(.*?)#", testdata)  # 如果没有找到就返回空列表
    # 标识符对应的值，；来自于：1，环境变量 2，配置文件   item：字符串 这两个地方的值必须都是字符串
    if res:
        for item in res:
            # 得到标识符对应的值
            try:
                value = con.get('general_user', item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    # value=item
                    continue
            # 再去替换原字符
            testdata = testdata.replace("#{}#".format(item), value)
    return testdata


# v1.0版本已经舍弃
def replace_lable(case, mark, real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换
    :param case:excel当中读取的一条数据 是一个字典
    :param mark:数据当中的一个占位符
    :param real_data:要替换mark的真实数据
    :return:
    """
    for key, value in case.items():
        # key不能为空，替换的动作只能是字符串，谁是谁的对象
        if case[key] is not None and isinstance(case[key], str):  # 确保是字符串
            if value.find(mark) != -1:  # 找到占位符，找到标识符
                case[key] = value.replace(mark, real_data)
    return case


if __name__ == '__main__':
    do = HandlerExcel(conf.excel, "recharge")
    res1 = do.read_all_datas()
    print(res1)
    user, password = get_old_phone()
    # 登陆接口调用
    data = {"mobile_phone": user, "pwd": password}
    res = send_request("POST", "/member/login", data).json()
    print(res)
    setattr(EnvData, "member_id", str(jsonpath(res, "$..id")[0]))
    setattr(EnvData, "token", jsonpath(res, "$..token"))
    res1 = replace_case_by_regular(res1)
    # print(json.dumps(res1,ensure_ascii=False))
