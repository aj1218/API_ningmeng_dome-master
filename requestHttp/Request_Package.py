"""
==========
Author:TT
Time:2021/2/23  4:16 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
基于项目做定制化封装
1：鉴权：token
2：项目通用的请求头：{ "X-Lemonban-Media-Type":"lemonban.v2"}
3:请求体格式：application/json
"""
import json

import requests
from jsonpath import jsonpath

from Outputs.Ini.ConfigParseCase import con
from Outputs.logs.logs import mylog
def __init__(self,msg):
    self.msg = msg

def send_request(method,url,data=None,token=None):
    mylog.info("发起一个http请求")
    #得到请求头
    headers = handle_header(token)
    url=__pre_url(url)
    #请求数据的处理 如果是字符串，则转换成字典对象
    data = __pre_data(data)
    mylog.info("请求头为：{}".format(headers))
    mylog.info("请求方法为：{}".format(method))
    mylog.info("请求url为：{}".format(url))
    mylog.info("请求数据为：{}".format(data))

    #根据请求类型，调用请求方法
    method=method.upper()
    if method == "GET":
        res = requests.get(url,params=data,headers=headers)
    elif method == "POST":
        res = requests.post(url, json=data, headers=headers)
    else:
        res = requests.request("PATCH", url, headers=headers, json=data)
    mylog.info("响应状态码为：{}".format(res.status_code))
    mylog.info("响应数据为：{}".format(res.json()))
    return res
def __pre_url(url):
    #拼接url地址
    base_url = con.get('server', 'base_url')
    if url.startswith("/"):
        return base_url + url
    elif url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return base_url + "/" + url

def __pre_data(data):
    """
    如果data是字符串 则转换为字典
    :param data:
    :return:
    """
    # if data is not None and isinstance(data,str):
    #     return json.loads(data)
    # return data

    if data is not None and isinstance(data,str):
        #如果有null，则替换为None
        if data.find("null")!=-1:
            #替换数据
            data = data.replace("null","None")
            #使用eval转换成为字典，eavl过程中，如果表达式有涉及计算，会自动计算
        data = eval(data)
    return data


def handle_header(token=None):
    headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers



if __name__ == '__main__':
    url = "member/login"
    data = {
    "mobile_phone":13577297771,
    "pwd":"123456789"
}
    res = send_request("POST",url,data).json()
    print(res)
    # res_dict=res.json()["data"]["token_info"]["token"]
    # print(res_dict)
    # menber_id = res.json()["data"]["id"]
    # print(menber_id)
    # token = jsonpath(res, '$..token')[0]
    # token_type = jsonpath(res, '$..token_type')[0]
    # menber_id = jsonpath(res, '$..id')[0]
    # recharge_url = "member/recharge"
    # recharge_data = {
    #     "member_id": menber_id,
    #     "amount": 10
    # }
    # # url=__pre_url(recharge_url)
    # recharge_res = send_request("POST",recharge_url, recharge_data,token=token)
    # print(recharge_res.json())