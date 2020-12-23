from BeautifulReport import BeautifulReport
import unittest
from TestCase.practice.test_http1 import TestHttp
import os
import time
from Base.setting import Setting
test_data = [{"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
              "data": {"mobile": "18688773467", "pwd": "123456"}, "expected": "1001", "method": "get"},
             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
              "data": {"mobile": "18688773467", "pwd": "12345689"}, "expected": "20111", "method": "post"},
             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
              "data": {"mobile": "18688773467", "amount": "1000"}, "expected": "10001", "method": "get"},
             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
              "data": {"mobile": "18688773467", "amount": "-100"}, "expected": "20117", "method": "post"},
             ]


report_path = os.path.join(Setting.BaseDir, 'Report')
suite = unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttp('test_api', item['url'], item['data'], item['method'], item['expected']))
if __name__ == '__main__':
    result = BeautifulReport(suite)
    result.report(filename='第一份测试报告' + str(time.time()), description='登录充值单元测试报告', report_dir=report_path,
                  theme='theme_default')
