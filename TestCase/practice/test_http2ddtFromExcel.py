import unittest
from tools.http_request import HttpRequest
from Base.setting import Setting
from ddt import ddt, unpack, data, file_data
from tools.get_data import LoadData
import os
from tools.readConfig import ReadConfig
CONFIG_PATH = os.path.join(os.path.join(Setting.BaseDir, 'Config'), 'case.config')
data_path = os.path.join(os.path.join(Setting.BaseDir, 'data\practiceData'),
                         ReadConfig().read_config(CONFIG_PATH, 'WORKBOOK', 'file_name'))
sheet_name = ReadConfig().read_config(CONFIG_PATH, 'WORKBOOK', 'sheet_name')
mode = ReadConfig().read_config(CONFIG_PATH, 'MODE', 'mode')

test_data_formal = LoadData(data_path, sheet_name).load_excel(mode)


@ddt
class TestHttp(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @data(*test_data_formal)
    def test_api(self, case_data):
        # print(case_data)
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



