"""
==========
Author:TT
Time:2021/3/5  3:58 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""

from jsonpath import jsonpath

from Outputs.logs.logs import mylog
from common.handler_data import EnvData


def extract_data_from_response(extrace_exprs, response_dict):
    """
    根据jsonpath 提取表达式，从响应结果当中，提取数据并设置为环境变量 EnvDta类的属性，作为全局变量使用
    :param extrace_exprs: 从excel当中读取出来的，提取表达式的字符串
    :param response_dict: http请求之后的响应结果
    :return: None
    """
    # 将提取表达式转换为字典
    extrace_dict = eval(extrace_exprs)
    mylog.info("要从响应结果当中提取的数据集为 ：\n{}".format(extrace_dict))

    # 遍历字典，key作为全局变量名，value是jsonpath的提取式。
    for key,value in extrace_dict.items():
        # 提取 上面的表达式里的数据一定要在替换的结果中有数据 不然就会报错
        res = str(jsonpath(response_dict,value)[0])
        print(res)
        # 设置提取之后的环境变量
        mylog.info("设置环境变量.key:{},value ：\n{}".format(key,res))
        setattr(EnvData, key, res)


if __name__ == '__main__':
    ss = '{"member_id":"$..id","token":"$..token"}'
    response = {'code': 0, 'msg': 'OK', 'data': {'id': 1000154511, 'token': '小柠檬', 'mobile_phone': '13480402544'}, 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
    extract_data_from_response(ss, response)
    print(EnvData.__dict__)
