"""
==========
Author:TT
Time:2021/2/5  3:44 下午
Project: API_ningmeng_dome
Company:自动化测试
==========
"""
import os
import unittest
import datetime
from logs import Mylog
mylog = Mylog(name="py301", file='my_logs.log')
from HTMLTestRunnerNew import HTMLTestRunner
from testcase.HttptestCase import TestCode


date = datetime.datetime.now().strftime("%Y-%m-%d%H%M")

suite=unittest.TestSuite()

loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCode))

report_file = os.path.join(date+"report1.html")

with open(report_file,"wb")as file:
    runner=HTMLTestRunner(stream=file, verbosity=2, title=None, description="这个是单元测试报告")
    runner.run(suite)



