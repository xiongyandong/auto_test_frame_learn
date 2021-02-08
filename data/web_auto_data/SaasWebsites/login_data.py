#  --*--coding: utf-8 --*--

# 1.正常登录场景
normal_data = {'login_name': '1078464470@qq.com', 'password': '123456'}

'''
异常场景1：
1.登录名不正确
2.密码不正确
'''
abnormal_data = [
    {'login_name': '1827081635@qq.com', 'password': '123456', 'check': 'Este usuário n?o exist'},
    {'login_name': '1078464470@qq.com', 'password': '1234569', 'check': 'Erro de senha'},
]