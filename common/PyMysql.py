"""
==========
Author:TT
Time:2021/2/25  4:48 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
mysql 数据库：pymysql
pip install pymysql
1：连接数据库 创建游标 获取一条数据，获取条数，获取所有数据，关闭数据库连接
2；执行sql语句
3：获取执行的结果
4；关闭数据库
"""
import pymysql
# #1：建立连接
# conn=pymysql.connect(
#     host="api.lemonban.com",
#     port=3306,
#     user="future",
#     password="123456",
#     database="futureloan",
#     charset="utf8",
#     cursorclass=pymysql.cursors.DictCursor
# )
# #创建游标
# cur = conn.cursor()
#
# #3:执行sql语句
# sql="SELECT *  FROM member limit 10"
# count=cur.execute(sql)
# print(count)
#
# #获取sql语句返回的数据，
# one =cur.fetchone() #获取数据
# print(one)
# print('---------------')
# two =cur.fetchone() #获取数据
# print(two)
# print('---------------')
# all = cur.fetchall()
# print(all)
from common.Case_file import conf
from Outputs.Ini.ConfigParseCase import con


class HandleDB:
    def __init__(self):
        # 连接数据库，创建游标
        self.conn = pymysql.connect(
            host=con.get('mysql', 'host'),
            port=con.getint('mysql', 'port'),
            user=con.get('mysql', 'user'),
            password=con.get('mysql', 'password'),
            database=con.get('mysql', 'database'),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def select_one_data(self, sql, args=None):
        self.conn.commit()
        self.cur.execute(sql,args)
        return self.cur.fetchone()

    def select_all_data(self, sql, args=None):
        self.conn.commit()
        self.cur.execute(sql, args)
        return self.cur.fetchall()

    def update(self, sql, args=None):
        # 对数据库进行增删改的操作
        self.cur.execute(sql, args)
        self.conn.commit()

    def get_count(self, sql, args=None):
        self.conn.commit()
        return self.cur.execute(sql, args)

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    # db = HandleDB()
    # sql = "SELECT *  FROM member limit 3;"
    # count=db.get_count(sql)
    # print("总条数",count)
    # one=db.select_one_data(sql)
    # print("一条数据",one)
    # all = db.select_all_data(sql)
    # print("多条数据", all)
    db = HandleDB()
    sql = "SELECT *  FROM member WHERE mobile_phone='13577297721';"
    from requestHttp.Request_Package import send_request

    data = {
        "method": "POST",
        "url": 'http://api.lemonban.com/futureloan/member/register',
        "data": {
            "mobile_phone": 13577297721,
            "pwd": "123456789"},
    }
    res = send_request(data["method"], data["url"], data["data"])
    print("响应结果", res.json())
    count = db.get_count(sql)
    print("获取数据为：", count)
