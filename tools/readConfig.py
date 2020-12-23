import configparser

#  配置文件读取出来的数据都是字符串
#  section option value  配置文件包含三个区域


class ReadConfig:
    @staticmethod
    def read_config(file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf.get(section, option)



