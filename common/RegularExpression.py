"""
==========
Author:TT
Time:2021/3/2  5:20 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
正则表达式
字符串查看，提取
"""
# 单字符匹配
# res=re.findall(".",s)
# print(res)

# res=re.findall("\d",s)
# print(res)

# res=re.findall("\D",s)
# print(res)

# res=re.findall("\w",s)
# print(res)

# res=re.findall("\W",s)
# print(res)

# res=re.findall("[qsd]",s)
# print(res)

# res=re.findall("[A-Za-z5-9]",s)
# print(res)


"""
正则手册：https://tool.oschina.net/uploads/apidocs/jquery/regexp.html
 . 匹配除“\n”之外的任何单个字符。
\d	匹配一个数字字符。等价于[0-9]。
\D	匹配一个非数字字符。等价于[^0-9]。
\w	匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”。 支持中文
\W	匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
[a-z]	字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
[xyz]	字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”。
[a-z]	字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
x|y	匹配x或y。例如，“z|food”能匹配“z”或“food”。“(z|f)ood”则匹配“zood”或“food”。

# 数量上的匹配
#{m} n是一个非负整数
#{n，m} 匹配前一个字符 至少n次 最多m次
#{n,}匹配前一个字符至少n次
* 匹配前一个字符 0次或者多次
+ 匹配前一个字符 1次或者多次
？ 匹配前一个字符 0次或者1次
贪婪模式：尽可能匹配更多更长 默认的贪婪模式
非贪婪模式：尽可能匹配更少
   改成非贪婪模式，在限定的数量表达式后面加一个？
   
 边界字符：
    ^ 开头的字符 以什么开头只匹配开头
    $ 结尾的字符 以什么结尾 只匹配结尾
    
() 匹配分组：将括号里面的匹配出来

"""
from common.handler_data import EnvData
from Outputs.Ini.ConfigParseCase import con
import re
# setattr(EnvData,"menber_id","12345666666")
# setattr(EnvData,"money","123")

# s = "qweratyuiaol#kjha332a&fd422a22a22a2asx柠檬"
# 提取
# res = re.findall("a(\d+)a", s)
# print(res)
data = '{"mobile_phone":"#user#","pwd":"#password#","type":1,"id":"#menber_id#","leave_amount":#money#}'

def regular_expression(data):
    # 通用
    res = re.findall("#(.*?)#", data) #如果没有找到就返回空列表
    # 标识符对应的值，；来自于：1，环境变量 2，配置文件
    for item in res:
        # 得到标识符对应的值
        try:
            velue = con.get("general_user", item)
        except:
            velue = getattr(EnvData, item)
        # 再去替换原字符
        data = data.replace("#{}#".format(item), velue)
    return data

if __name__ == '__main__':
    re=regular_expression(data)
    print(re)

















