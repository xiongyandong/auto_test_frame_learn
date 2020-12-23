import unittest
from tools.http_request import HttpRequest
from Base.setting import Setting


class TestHttp(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        self.recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'

    def __init__(self, methodName, url, data, method, expected):
        super(TestHttp,self).__init__(methodName)  # 重写父类方法 保留父类__init__ 方法属性 又添加自己子类的属性
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected
    def test_api(self):
        # data = {"mobile": "18688773467", "pwd": "123456"}
        res = HttpRequest().general_request(self.method, self.login_url, self.data)
        if res.cookies:
            setattr(Setting, 'Cookie', res.cookies)
        try:
            self.assertEqual(self.expected,res.json()['code'])
        except AssertionError as e:
            print("test_api's error is {}".format(e))
            raise e
        print(res.json())


    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
