# --*-- coding :utf-8 --*--
# @Time: 2021/2/23 17:30
# @User: root
# @IDE: PyCharm
# @Author : xyd_boss
# @File: conftest.py

import pytest
import warnings
from selenium import webdriver
from data.web_auto_data.SaasWebsites import common_data
from tools.project_path import SaaSWebsitePath as sp
from PageObjects.login_page import LoginPage
import time
driver = None
lg =None


@pytest.fixture(scope='class')
def access_web():
    # 前置操作
    global driver
    global lg
    print("同一个测试类中所有用例执行前的操作，只执行一次")
    warnings.simplefilter('ignore', ResourceWarning)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=options)
    driver.maximize_window()
    driver.get(common_data.web_login_url)
    lg = LoginPage(driver, sp.login_log_path, sp.screenshot_path)
    yield (driver, lg)
    # 后置操作
    print('同一个测试类中所有用例执行之后，整个类只执行一次')
    driver.quit()


@pytest.fixture()
def refresh_page():
    # 前置操作为空
    global driver
    global lg
    time.sleep(2)
    lg.logs.my_log('我已经等待啦', 'INFO')
    yield
    # 后置操作
    driver.refresh()
    lg.logs.my_log('我已经刷新啦', 'INFO')

