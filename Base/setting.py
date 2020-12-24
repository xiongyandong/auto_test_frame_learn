# --*--coding:utf-8 --*--
import os

class Setting:
    Cookie = None
    BaseDir = os.path.dirname(os.path.dirname(__file__))
    From_user = '1078464470@qq.com'
    From_user_pwd = 'ktxelsdnlmengcdj'
    Email_Host = 'smtp.qq.com'
    To_user = 'xiongyandong@meorient.com'


if __name__ == '__main__':
    print(Setting.BaseDir)
