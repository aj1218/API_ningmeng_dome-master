"""
==========
Author:TT
Time:2021/2/26  3:37 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
手机号随机生成
1：随机生成一个11为的手机号 前三位+后8位
2；进行数据库校验
"""
import json

prefix = [149, 153, 173, 177, 180, 189,
          130, 131, 132, 145, 155, 156, 176, 185, 186, 166,
          134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182]
import random
from common.PyMysql import HandleDB
from Outputs.Ini.ConfigParseCase import con
from requestHttp.Request_Package import send_request


def get_new_phone():
    db = HandleDB()
    while True:
        # 1:生成
        generator = __generator_phone()
        # 2：校验
        sql = "SELECT *  FROM member WHERE mobile_phone=%s;"
        count = db.get_count(sql, args=[generator])
        if count == 0:  # 手机号么有在数据库查到 就退出循坏
            db.close()
            return generator


def __generator_phone():
    index = random.randint(0, len(prefix) - 1)
    phone = str(prefix[index])
    for i in range(0, 8):
        phone += str(random.randint(0, 9))
    return phone


# print(__generator_phone())

def check_sql_in_db(phone):
    """
    如果手机号不存在，那ok，如果存在得重新生成一次
    :param phone:
    :return:
    """
    pass


def get_old_phone():
    """
    从配置文件或者指定的用户名个密码
    :return:
    """
    user = con.get('general_user', "user")
    password = con.get('general_user', "password")
    print(type(user), type(password))
    # 如果数据库查到了就找到user，直接返回，则调用注册接口注册一个
    # 不管注册与否，直接调用注册接口
    recharge_data = {"mobile_phone": user, "pwd": password}
    send_request("POST", "member/register", recharge_data)
    return user, password


if __name__ == '__main__':
    res=get_old_phone()
    print(res)