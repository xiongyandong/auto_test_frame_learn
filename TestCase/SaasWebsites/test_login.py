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


def test_demo():
    print('我是demo函数.......................')


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--no-sandbox')
        options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        cls.drive = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                                  options=options)
        cls.drive.maximize_window()
        cls.drive.get(common_data.web_login_url)
        cls.lg = LoginPage(cls.drive, sp.login_log_path, sp.screenshot_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.drive.quit()

    def setUp(self) -> None:
        time.sleep(2)
        self.lg.logs.my_log('我已经等待啦', 'INFO')

    def tearDown(self) -> None:
        self.drive.refresh()
        self.lg.logs.my_log('我已经刷新啦', 'INFO')

    def test_2_login_success(self):
        self.lg.login(login_data.normal_data['login_name'], login_data.normal_data['password'])
        time.sleep(2)
        self.assertTrue(IndexPage(self.drive, sp.index_log_path, sp.screenshot_path).isExist_login_ele())

    @data(*login_data.abnormal_data)
    def test_1_wrong_loginName_pwd(self, wrong_data):
        self.lg.login(wrong_data['login_name'], wrong_data['password'])
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), wrong_data['check'])



if __name__ == '__main__':
    unittest.main()
