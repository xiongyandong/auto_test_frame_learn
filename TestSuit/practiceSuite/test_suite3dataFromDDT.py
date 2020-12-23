from BeautifulReport import BeautifulReport
import unittest
# from TestCase.test_meorient import TestHttp
# from TestCase import test_meorient
# from TestCase.test_http import TestHttp
# from TestCase import test_http
# from TestCase.test_http1 import TestHttp
from TestCase.practice.test_http2ddtFromExcel import TestHttp
# from TestCase.test_http2ddtFromjson import TestHttp
# from TestCase.test_http2ddtFromyaml import TestHttp
import os
import time
from Base.setting import Setting


if __name__ == '__main__':
    report_path = os.path.join(Setting.BaseDir, 'Report')
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestHttp))
    result = BeautifulReport(suite)
    result.report(filename='第一份测试报告' + str(time.time()), description='登录充值单元测试报告', report_dir=report_path,
                  theme='theme_default')
