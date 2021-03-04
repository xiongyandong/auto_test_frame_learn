import unittest
from ddt import ddt, data
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from data.web_auto_data.SaasWebsites import login_data
from data.web_auto_data.SaasWebsites import common_data
from tools.project_path import SaaSWebsitePath as sp
import time
import warnings
import pytest


# @pytest.mark.demo
# def test_demo():
#     print('我是demo函数.......................')
#     assert True


@pytest.mark.py
@pytest.mark.usefixtures('access_web')
@pytest.mark.usefixtures('refresh_page')
class TestLogin:

    @pytest.mark.parametrize('wrong_data', login_data.abnormal_data)
    def test_1_wrong_loginName_pwd(self, wrong_data, access_web):
        access_web[1].login(wrong_data['login_name'], wrong_data['password'])
        assert access_web[1].get_errorMsg_from_loginArea() == wrong_data['check']

    def test_2_login_success(self, access_web):
        access_web[1].login(login_data.normal_data['login_name'], login_data.normal_data['password'])
        time.sleep(2)
        assert IndexPage(access_web[0], sp.index_log_path, sp.screenshot_path).isExist_login_ele()


if __name__ == '__main__':
    pytest.main()


