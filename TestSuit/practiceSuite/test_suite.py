from BeautifulReport import BeautifulReport
import unittest
from TestCase.practice.test_http import TestHttp
import os
import time
from Base.setting import Setting
report_path = os.path.join(Setting.BaseDir, 'Report')
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttp))
if __name__ == '__main__':

    result = BeautifulReport(suite)
    result.report(filename='第一份测试报告'+str(time.time()), description='登录充值单元测试报告', report_dir=report_path,
                  theme='theme_default')
