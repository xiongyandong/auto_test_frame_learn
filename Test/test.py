# tel = '13654541214'
# a = tel.find('6')
# print(a)

#
# t1 = time.time()
#
# time.sleep(2.5)
# t2 = time.time()
# t = t2-t1
# print('{:.2f}'.format(t))
# print(format(t, '.2f'))


# def a_new_decorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
#
# a_function_requiring_decoration()
# print(a_function_requiring_decoration.__name__)


# def attached(_func):
#     # 对basePage中封装的基本元素操作输出日志及截图
#     @wraps(_func)
#     def log_with_screenshot(loc, doc):
#         t1 = time.time()
#         try:
#             _func(loc, doc)
#             time.sleep(2.02)
#         except Exception as e:
#             logs.my_log(e, 'ERROR')
#             # 截图
#             # saveScreenshot(doc)
#             raise e
#         t2 = time.time()
#         print(t2-t1)
#
#     return log_with_screenshot
#
#
# @attached
# def test(loc, doc):
#     loc * doc
#     print(loc, doc)
#
#
