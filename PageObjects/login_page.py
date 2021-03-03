from Base.base_Page import Page
from LocatorEmelent.SassWebsites.loginPageLocatorEmelent import *


class LoginPage(Page):
    doc = 'login'

    def login(self, username, pwd):
        # 输入用户名
        # 输入密码
        # 点击提交
        self.wait_eleVisible(sign_in_ele, doc=self.doc)
        self.click(sign_in_ele, self.doc)
        self.input_text(name_ele, username, self.doc)
        self.input_text(pwd_ele, pwd, self.doc)
        self.click(login_button, self.doc)

    def get_errorMsg_from_loginArea(self):
        self.wait_eleVisible(loinNameOrPasswordErrorToast, doc=self.doc)
        return self.get_text(loinNameOrPasswordErrorToast, self.doc)
