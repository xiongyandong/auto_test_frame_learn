from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
drive = webdriver.Chrome(service_log_path='service.log')
# 全局等待等待元素得出现
# drive.implicitly_wait(30)
import time
# drive.get('https://www.baidu.com')
# # 窗口最大化
# drive.maximize_window()
# drive.find_element_by_id('kw')
# drive.find_element_by_class_name()
# drive.get('http://www.taobao.com')
# # 回退上一页
# drive.back()
# # 回到下一页
# drive.forward()
# # 刷新
# drive.refresh()
# # 获取标题
# print(drive.title)
# # 获取网址
# print(drive.current_url)
# # 当前窗口的句柄（id)
# print(drive.current_window_handle)
drive.get('http://testcity.tradechina.com/poland')
drive.maximize_window()
drive.find_element_by_class_name('Header_loginBtn__3_BKD').click()
drive.find_element(By.XPATH,'//div[@class="verify-input Header_loginInput__1KA74"]/input[@type="text"]').send_keys('1078464470@qq.com')
drive.find_element(By.XPATH, '//div[@class="verify-input Header_loginInput__1KA74"]/input[@type="password"]').send_keys('123456')
drive.find_element(By.CLASS_NAME, 'meo-button').click()
time.sleep(2)
print(drive.find_element(By.XPATH, '//a[@class="Header_accountCon__2w8S3"]').text)