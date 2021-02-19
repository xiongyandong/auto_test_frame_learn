# --*--coding:utf-8 --*--
from tools.log import MyLog
import time
import datetime
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    """
    page 为基类，所有页面都应继承这个页面 真正框架中basePage应该单独放在common包里面，common包为本框架通用内容，可放在项目顶层目录，如本框架
    中的Base模块
    doc参数代表的是各个具体页面，以便后期存储截图区分图片的路径
    """

    def __init__(self, drive, log_file, screen_shot_file):
        self.drive = drive
        self.timeout = 30
        self.logs = MyLog(log_file)
        self.screen_shot_file = screen_shot_file

    def find_element(self, loc, doc=''):
        self.logs.my_log('查找元素{}'.format(loc), 'INFO')
        try:
            return self.drive.find_element(*loc)
        except:
            self.logs.my_log('等待元素可见失败！！！', 'ERROR')
            # 截图
            self.saveScreenshot(doc)
            raise

    def input_text(self, loc, text, doc=''):
        ele = self.find_element(loc, doc)
        try:
            ele.send_keys(text)
        except:
            self.logs.my_log('元素输入操作失败！！！', 'ERROR')
            # 截图
            self.saveScreenshot(doc)
            raise

    def click(self, loc, doc=''):
        # 找元素
        # 对元素进行操作
        ele = self.find_element(loc, doc)
        self.logs.my_log('点击元素：{}'.format(loc), 'INFO')
        try:
            ele.click()
            import time
            time.sleep(2)
            self.saveScreenshot(doc)
        except:
            self.logs.my_log('等待元素点击失败！！！', 'ERROR')
            # 截图
            self.saveScreenshot(doc)
            raise

    def get_title(self, doc=''):
        try:
            return self.drive.title
        except:
            self.logs.my_log('获取页面title失败', 'ERROR')
            self.saveScreenshot(doc)
            raise

    def get_text(self, loc, doc=''):
        # 获取文本内容
        ele = self.drive.find_element(loc, doc)
        try:
            return ele.text
        except:
            self.logs.my_log('获取元素文本失败', 'ERROR')
            self.saveScreenshot(doc)
            raise

    def get_element_attribute(self, loc, attr, doc=''):
        # 获取元素的属性值
        ele = self.find_element(loc, doc)
        try:
            return ele.get_attribute(attr)
        except:
            self.logs.my_log('获取元素属性失败', 'ERROR')
            self.saveScreenshot(doc)
            raise

    def wait_eleVisible(self, loc, waitTime=20, doc=''):
        # 等待元素可见
        self.logs.my_log('等待元素 {} 可见'.format(loc), 'INFO')
        try:
            t1 = time.time()
            WebDriverWait(self.drive, waitTime).until(EC.visibility_of_element_located(loc))
            t2 = time.time()
            wait_for_elements_takes_time = '{:.2f}'.format(t2-t1)   # 等待元素耗费时间
            self.logs.my_log('等待结束，等待时常为{}'.format(wait_for_elements_takes_time), 'INFO')
        except:
            print('没有可见元素')
            self.logs.my_log('等待元素可见失败！！！', 'ERROR')
            self.saveScreenshot(doc)
            raise

        pass

    def wait_elePresence(self):
        # 等待元素存在
        pass

    def alert_action(self, action='accept'):
        # alert处理
        pass

    def switch_iframe(self, iframe_reference):
        # iframe切换
        pass

    def upload_file(self):
        # 上传操作
        pass

    def saveScreenshot(self, name):
        # 截图操作
        # 图片名称：模块名_页面名称_操作名称_时间.jpg
        now_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')  # 将日期格式转化成字符串格式
        file_name = os.path.join(os.path.join(self.screen_shot_file, name), '{}_{}.png'.format(name, now_time))
        try:
            self.drive.save_screenshot(file_name)
            self.logs.my_log('截屏成功，文件路径为{}'.format(file_name), 'INFO')
        except Exception as e:
            raise e
