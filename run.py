#coding:utf-8
import sys

sys.path.append("../..")
import unittest
from common.Case_file import conf
from HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.discover(conf.test_case))

with open(conf.HTML, "wb")as file:
    runner = HTMLTestRunner(stream=file, verbosity=2, title=None, description="这个是单元测试报告")
    runner.run(suite)
