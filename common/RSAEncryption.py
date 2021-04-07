"""
==========
Author:TT
Time:2021/3/12  3:11 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
import base64

import rsa
from time import time

from jsonpath import jsonpath


def rsaEncrypt(msg):
    """
    公钥加密
    :param msg: 要加密的内容
    ：type msg：str
    :return: 加密之后的内容
    """
    server_pub_key = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
kKlZFc8Br7SHtbL2tQIDAQAB 
-----END PUBLIC KEY-----
    """


    # 生成公钥对象、
    pub_key_byte = server_pub_key.encode("utf-8")
    print(pub_key_byte)
    pub_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_byte)

    # 要加密的数据转成字节对象
    content = msg.encode("utf-8")
    print(content)

    # 加密，返回加密文本
    cryto_msg = rsa.encrypt(content,pub_key_obj)

    # base64编码
    cipher_base64 = base64.b64decode(cryto_msg)
    print("1",cipher_base64)
    # 转成字符串
    return cipher_base64.decode()


def generator_sign(token):
    # 获取tekon的前50位
    tekon_50 = token[:50]
    # 生成时间戳
    timestamp = int(time())
    print(timestamp)
    # 拼接token前50位和时间戳
    msg = tekon_50 + str(timestamp)
    print(msg)
    # 进行RSA加密
    sign = rsaEncrypt(msg)
    return sign, timestamp


if __name__ == '__main__':
    import requests

    headers = {"X-Lemonban-Media-Type": "lemonban.v3"}
    login_url = "http://api.lemonban.com/futureloan/member/login"
    login_data = {
    "mobile_phone":"15312341234",
    "pwd":"123456789"
}
    # url=__pre_url(recharge_url)
    res = requests.request("POST",login_url, json=login_data,headers=headers).json()
    token = jsonpath(res, '$..token')[0]
    menber_id = jsonpath(res, '$..id')[0]

    headers["Authorization"] = "Bearer {}".format(token)
    sign, timestamp=generator_sign(token)
    print("签名为： ",sign,"\n时间戳为： ",timestamp)

    recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    recharge_data = {
        "member_id": menber_id,
        "amount": 10,
        "sign":sign,
        "timestamp":timestamp
    }
    # url=__pre_url(recharge_url)
    recharge_res = requests.request("POST",login_url, json=login_data,headers=headers)
    print(recharge_res.json())

