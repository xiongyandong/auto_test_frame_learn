
import unittest
from tools.http_request import HttpRequest
from Base.setting import Setting


class TestHttp(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = 'http://testoperation.chinahomelife247.com/login.json'

    def test_login_normal(self):
        data = {"username": "superadmin", "password": "123456"}
        res = HttpRequest().general_request('post', self.login_url, data)
        if res.cookies:
            print(res.cookies)
            setattr(Setting, 'Cookie', res.cookies)
        self.assertEqual(201, res.status_code)

    def test_login_wrong_pwd(self):
        data = {"username": "superadmin", "password": "12345689"}
        res = HttpRequest().general_request('post', self.login_url, data)
        print(res.json())
        if res.cookies:
            print(res.cookies)
            setattr(Setting, 'Cookie', res.cookies)
        self.assertEqual('Password is incorrect', res.json()['errors']['errors'][0]['message'])

    # def test_recharge_normal(self):
    #     recharge_data = {"mobile": "18688773467", "amount": "1000"}
    #     res = HttpRequest().general_request('post', self.recharge_url, recharge_data, cookie=getattr(Setting, 'Cookie'))
    #
    # def test_recharge_negative(self):
    #     recharge_data = {"mobile": "18688773467", "amount": "-100"}
    #     res = HttpRequest().general_request('post', self.recharge_url, recharge_data, cookie=getattr(Setting, 'Cookie'))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
