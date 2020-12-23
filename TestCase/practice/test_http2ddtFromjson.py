import unittest
from tools.http_request import HttpRequest
from Base.setting import Setting
from ddt import ddt, unpack, data, file_data
from tools.get_data import LoadData
import os

data_path = os.path.join(os.path.join(Setting.BaseDir, 'data'), 'testdata.json')


@ddt
class TestHttp(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @file_data(data_path)
    def test_api(self, **case_data):
        res = HttpRequest().general_request(case_data['method'], case_data['url'], case_data['data'])
        if res.cookies:
            setattr(Setting, 'Cookie', res.cookies)
        try:
            self.assertEqual(case_data['expected'], res.json()['code'])
        except AssertionError as e:
            print("test_api's error is {}".format(e))
            raise e
        print(res.json())

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
