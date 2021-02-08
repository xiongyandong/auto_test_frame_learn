from Base.base_Page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LocatorEmelent.SassWebsites.loginPageLocatorEmelent import *
import time


class LoginPage(Page):
    def login(self, username, pwd):
        # 输入用户名
        # 输入密码
        # 点击提交
        WebDriverWait(self.drive, 20).until(EC.visibility_of_element_located(sign_in_ele))
        self.click(sign_in_ele)
        self.input_text(name_ele, username)
        self.input_text(pwd_ele, pwd)
        self.click(login_button)

    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.drive, 20).until(EC.visibility_of_element_located(loinNameOrPasswordErrorToast))
        return self.find_element(loinNameOrPasswordErrorToast).text



