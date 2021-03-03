# from openpyxl import load_workbook
# wb = load_workbook(path)
#
# sheet = wb['python']
# value = sheet.cell(1, 4).value
# max_row = sheet.max_row
# max_column = sheet.max_column
import os
import time
import datetime
from BeautifulReport import BeautifulReport
from TestSuit.p2pSuite.test_suite_dataFromDDT import TestSuit
from TestSuit.SaaSwebsites.perform_suit import SaaSwebsiteSuit
from TestCase.SaasWebsites.test_login import TestLogin
from tools.to_email import SendEmail
from tools.project_path import ProjectPath, SaaSWebsitePath

if __name__ == '__main__':
    # _type = input('接口测试输入1， ui测试输入2： ')
    # if _type == '1':
    report_path = ProjectPath.p2p_report_path
    report_name = 'p2p测试报告'+str(time.time())+'.html'
    suites = TestSuit().make_suite_by_loader()
    result = BeautifulReport(suites)
    result.report(filename=report_name, description='登录充值单元测试报告', report_dir=report_path,
                  theme='theme_cyan')
    filepath = os.path.join(report_path, report_name)
    if filepath:
        SendEmail.send_email(filepath)
    # elif _type == '2':
    #     report_path = SaaSWebsitePath.saaswebsite_report_path
    #     report_name = 'ui测试报告'+datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.html'
    #     suites = SaaSwebsiteSuit().make_suite_by_loader(TestLogin)
    #     result = BeautifulReport(suites)
    #     result.report(filename=report_name, description='saas站登录测试报告', report_dir=report_path,
    #                   theme='theme_cyan')
    #     filepath = os.path.join(report_path, report_name)
    #     if filepath:
    #         SendEmail.send_email(filepath)



