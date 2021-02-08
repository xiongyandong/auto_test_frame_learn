# --*-- coding = utf-8 --*--
from selenium.webdriver.common.by import By

sign_in_ele = (By.CLASS_NAME, 'Header_loginBtn__3_BKD')
name_ele = (By.XPATH, '//div[@class="verify-input Header_loginInput__1KA74"]/input[@type="text"]')
pwd_ele = (By.XPATH, '//div[@class="verify-input Header_loginInput__1KA74"]/input[@type="password"]')
login_button = (By.CLASS_NAME, 'meo-button')
loinNameOrPasswordErrorToast = (By.CLASS_NAME, 'za-toast__container')