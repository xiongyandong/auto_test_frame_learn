# configparser  可以读取配置信息  其他包含 properties  config  ini  log4j 等结尾的文件
import configparser
#  配置文件读取出来的数据都是字符串
#  section option value  配置文件包含三个区域

cf = configparser.ConfigParser()
cf.read('case.config', encoding='utf-8')

# 读取配置文件数据
res_1 = cf.get('MODE', 'mode')  # 需传section和option两个参数
print(res_1)

res_2 = cf['MODE']['mode']
print(res_2)

print(cf.sections())
print(cf.items('PYTHON11'))  # 取到某个片区下的option和value,存在一个元组里面并返回多个元组组成的列表
