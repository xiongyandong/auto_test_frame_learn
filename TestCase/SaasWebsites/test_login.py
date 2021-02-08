import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from data.web_auto_data.SaasWebsites import login_data
from data.web_auto_data.SaasWebsites import common_data
import time


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.drive = webdriver.Chrome()
        cls.drive.maximize_window()
        cls.drive.get(common_data.web_login_url)
        cls.lg = LoginPage(cls.drive)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.drive.quit()

    def setUp(self) -> None:
        time.sleep(2)
        print('我已经等待啦')

    def tearDown(self) -> None:
        self.drive.refresh()
        print('我已经刷新啦')

    def test_2_login_success(self):
        self.lg.login(login_data.normal_data['login_name'], login_data.normal_data['password'])
        time.sleep(2)
        self.assertTrue(IndexPage(self.drive).isExist_login_ele())

    @data(*login_data.abnormal_data)
    def test_1_wrong_loginName_pwd(self, wrong_data):
        print(wrong_data)
        self.lg.login(wrong_data['login_name'], wrong_data['password'])
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), wrong_data['check'])


if __name__ == '__main__':
    unittest.main()
