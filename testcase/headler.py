"""
==========
Author:TT
Time:2021/2/5  3:43 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
class Headler:
    def testHeadler(self,username=None,pwd=None):
        if username !=None and pwd !=None:
            if username =="python30" and pwd ==11111:
                code= {"msg":"登陆成功","code":0}
                return code
            else:
                code = {"msg":"登陆失败","code":1}
                return code
        else:
            code = {"msg": "所有参数不能为空"}
            return code
