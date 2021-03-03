# --*-- coding:utf-8 --*--
import requests
from tools.log import MyLog
from tools.project_path import ProjectPath
my_log = MyLog(ProjectPath.p2p_log_path)

class HttpRequest:
    def __init__(self):
        pass

    def general_request(self, method, url, param, cookie=None):
        try:
            if method.lower() == 'get':
                return requests.session().get(url=url, params=param, cookies=cookie, verify=False)
            elif method.lower() == 'post':
                return requests.session().post(url=url, data=param, cookies=cookie,verify=False)

            else:
                my_log.my_log('输入的请求方法不对', 'INFO')
        except Exception as e:
            my_log.my_log('请求报错了', 'ERROR', )
            raise e


# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# file_path = os.path.join(base_dir,'data','testdata.json')

# {
#     "first":["{'name':'tom','age':15}","200"],
#     "two":["{'name':'jack','age':18}","404"],               这是一个字典，在ddt中也是不能再拆分的对象，故用unpack也不能使其拆解
#     "three":["{'name':'marry','age':8}","200"]
# }

if __name__ == '__main__':
    HttpRequest().general_request('get', '10.21.64.31:8080/login', param=None)