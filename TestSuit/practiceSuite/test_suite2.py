from BeautifulReport import BeautifulReport
import unittest
from TestCase.practice.test_http1 import TestHttp
import os
import time
from Base.setting import Setting
from tools.get_data import LoadData

if __name__ == '__main__':
    report_path = os.path.join(Setting.BaseDir, 'Report')
    data_path = os.path.join(os.path.join(Setting.BaseDir, 'data'), 'test.xlsx')
    suite = unittest.TestSuite()
    test_data_formal = LoadData(data_path, 'python').load_excel()
    print(test_data_formal)
    for item in test_data_formal:
        suite.addTest(TestHttp('test_api', item['url'], item['data'], item['method'], item['expected']))
    result = BeautifulReport(suite)
    result.report(filename='第一份测试报告' + str(time.time()), description='登录充值单元测试报告', report_dir=report_path,
                  theme='theme_default')
