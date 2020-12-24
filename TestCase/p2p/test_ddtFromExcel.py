import unittest
from tools.http_request import HttpRequest
from Base.setting import Setting
from ddt import ddt, unpack, data, file_data
from tools.get_data_from_p2p import *

from tools.project_path import ProjectPath
load_object = LoadData(ProjectPath.p2p_data_path, ProjectPath.p2p_module)
test_data_formal = load_object.load_excel()


@ddt
class TestHttp(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @data(*test_data_formal)
    def test_api(self, case_data):
        print(case_data)
        load_object.write_back(case_data['module'], case_data['case_id'] + 1, 8, case_data['expected'])
        try:
            self.assertEqual(case_data['expected'], 1001)
            load_object.write_back(case_data['module'], case_data['case_id'] + 1, 9, 'Pass')
        except AssertionError as e:
            load_object.write_back(case_data['module'], case_data['case_id'] + 1, 9, 'Fail')
            MyLog().my_log(e, 'ERROR')
            # raise e
        # res = HttpRequest().general_request(case_data['method'], case_data['url'], case_data['data'])
        # if res.cookies:
        #     setattr(Setting, 'Cookie', res.cookies)
        # try:
        #     self.assertEqual(case_data['expected'], res.json()['code'])
        # except AssertionError as e:
        #     print("test_api's error is {}".format(e))
        #     raise e
        # print(res.json())

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    print(test_data_formal)

