# --*--coding:utf-8 --*--
from tools.log import MyLog


class Page:
    """
    page 为基类，所有页面都应继承这个页面 真正框架中basePage应该单独放在common包里面，common包为本框架通用内容，可放在项目顶层目录，如本框架
    中的Base模块
    """

    def __init__(self, drive, log_file):
        self.drive = drive
        self.timeout = 30
        self.logs = MyLog(log_file)

    def find_element(self, loc, doc=''):
        self.logs.my_log('查找元素{}'.format(loc), 'INFO')
        try:
            return self.drive.find_element(*loc)
        except:
            self.logs.my_log('等待元素可见失败！！！', 'EXCEPTION')
            # 截图
            self.save_screenshot(doc)
            raise

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def click(self, loc, doc=''):
        # 找元素
        # 对元素进行操作
        ele = self.find_element(loc, doc)
        self.logs.my_log('点击元素：{}'.format(loc), 'INFO')
        try:
            ele.click()
        except:
            self.logs.my_log('等待元素点击失败！！！', 'EXCEPTION')
            # 截图
            self.save_screenshot(doc)
            raise


    def get_title(self):
        return self.drive.title

    def get_text(self, loc):
        # 获取文本内容
        return self.drive.find_element(loc).text

    def get_element_attribute(self):
        # 获取元素的属性值
        pass

    def wait_eleVisible(self):
        # 等待元素可见
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

    def save_screenshot(self, name):
        # 截图操作
        # 图片名称：模块名_页面名称_操作名称_时间.jpg
        time = ''
        file_name = '截屏存放的路径' + '{}_{}.png'.format(name, time)
        try:
            self.drive.save_screenshot(file_name)
            MyLog().my_log('截屏成功，文件路径为{}'.format(file_name), 'INFO')
        except Exception as e:
            raise e
