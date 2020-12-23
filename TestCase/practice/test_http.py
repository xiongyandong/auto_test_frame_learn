import unittest
from tools.http_request import HttpRequest
from Base.setting import Setting


class TestHttp(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        self.recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'

    def test_login_normal(self):
        data = {"mobile": "18688773467", "pwd": "123456"}
        res = HttpRequest().general_request('GET', self.login_url, data)
        if res.cookies:
            setattr(Setting, 'Cookie', res.cookies)

    def test_login_wrong_pwd(self):
        data = {"mobile": "18688773467", "pwd": "12345689"}
        res = HttpRequest().general_request('GET', self.login_url, data)

    def test_recharge_normal(self):
        recharge_data = {"mobile": "18688773467", "amount": "1000"}
        res = HttpRequest().general_request('post', self.recharge_url, recharge_data, cookie=getattr(Setting, 'Cookie'))

    def test_recharge_negative(self):
        recharge_data = {"mobile": "18688773467", "amount": "-100"}
        res = HttpRequest().general_request('post', self.recharge_url, recharge_data, cookie=getattr(Setting, 'Cookie'))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
