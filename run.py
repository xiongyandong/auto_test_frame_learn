# from openpyxl import load_workbook
# wb = load_workbook(path)
#
# sheet = wb['python']
# value = sheet.cell(1, 4).value
# max_row = sheet.max_row
# max_column = sheet.max_column
import os
import time
from BeautifulReport import BeautifulReport
from TestSuit.p2pSuite.test_suite_dataFromDDT import TestSuit
from tools.to_email import SendEmail
from tools.project_path import ProjectPath

if __name__ == '__main__':
    report_path = ProjectPath.p2p_report_path
    report_name = 'p2p测试报告'+str(time.time())+'.html'
    suites = TestSuit().make_suite_by_loader()
    result = BeautifulReport(suites)
    result.report(filename=report_name, description='登录充值单元测试报告', report_dir=report_path,
                  theme='theme_cyan')
    filepath = os.path.join(report_path, report_name)
    if filepath:
        SendEmail.send_email(filepath)





