from Base.base_Page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LocatorEmelent.SassWebsites.indexPageLocatorEmelent import *
import time


class IndexPage(Page):
    def isExist_login_ele(self):
        # 获取登陆成功后的标志，即登录名
        try:
            WebDriverWait(self.drive, 20).until(EC.visibility_of_element_located(login_icon))
            user_name = self.find_element(login_icon).text
            print(user_name)
            if user_name == 'xiong yd yd':
                return True
            else:
                return False
        except Exception as e:
            raise e


