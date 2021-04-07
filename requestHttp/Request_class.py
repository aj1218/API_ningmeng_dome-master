"""
==========
Author:TT
Time:2021/2/22  5:14 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
import requests
class RequestHandler:
    """
    get：param
    没有请求体，param就是追加在url后面的查询参数
    接口地址？key=value&key=value&。。。。
    {"status":1,"code":10000,"message":"\u8bbf\u95ee\u6210\u529f",
    "data":{"url":"",
    "token":"e74b06b0cce0b7c3d59d08d4cbf6ce3ee0000f58b6e08531a6e8d12d332ff5ab",
    "isenterprise":0,"uid":"MDAwMDAwMDAwMLR2vZeH36uvhctyoQ"}}

    第二步：获取用户信息
    接口url：https://openapiv5.ketangpai.com/UserApi/login
    请求方式：get
    请求参数：无


    Session类：创建一个会话对象
    """
import requests

# #第一步；
# s=requests.Session()
#
# print("登陆之前的cookies：",s.cookies)
# #第二步：登陆，得到cookies
# login_url = 'https://openapiv5.ketangpai.com/UserApi/login'
#
# data = {
#     "email": "15388030234",
#     "password": "qq977089471",
#     "remember": "0"
# }
# res = s.post(login_url,json=data)
# print("响应的cookies",res.cookies)
# print("登陆之后的cookies",s.cookies)#主动会将set_cookies 添加到s对象当中
#
# #第二步获取用户信息
# info_url = "https://openapiv5.ketangpai.com/UserApi/getUserBasinInfo"
# info = s.get(info_url)
# print(info.json())
#data {'id': 10019019, 'leave_amount': 0.0,
# 'mobile_phone': '13577797773', 'reg_name': '小柠檬',
# 'reg_time': '2021-02-23 15:14:02.0', 'type': 1,
# 'token_info': {'token_type': 'Bearer',
# 'expires_in': '2021-02-23 15:30:41',
# 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMDE5MDE5LCJleHAiOjE2MTQwNjU0NDF9.fhBVZB98KngNnM5saKNdrjUf6Y6YtVibeGtehj27rLZxov9uNDw1uZAY_vNJGBL318ixrN9ofUwXPYlOI5znLA'}}

url = 'http://api.lemonban.com/futureloan/member/login'
data = {
    "mobile_phone":13577797773,
    "pwd":"123456789"

}
headers = {
    "X-Lemonban-Media-Type":"lemonban.v2"
}
res = requests.post(url,json=data,headers=headers)
# for key,value in res.json().items():
#     print(key,value)
res_dict = res.json()
toeken = res_dict["data"]["token_info"]["token"]
menber_id = res_dict["data"]["id"]
print(toeken)

# 第二步 充值；将token 添加到请求头当中
headers["Authorization"] = "Bearer {}".format(toeken)
print(headers)
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
recharge_data={
    "member_id":menber_id,
    "amount":10
}
recharge_res = requests.post(recharge_url,json=recharge_data,headers=headers)
print(recharge_res.json())
