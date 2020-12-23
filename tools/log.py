import logging
from Base.setting import Setting
import os
# logging.debug('hhhh')
# logging.info('ll')
# logging.warning('无了')
# logging.error('报错了')
# logging.critical('hsaj')


class MyLog:
    logPath = os.path.join(Setting.BaseDir, r'Logs\p2pLog\test.txt')
    my_logger = logging.getLogger('myLog')
    fh = logging.FileHandler(logPath, encoding='utf-8')
    formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")

    def my_log(self, msg, level):
        self.my_logger.setLevel(level)
        self.fh.setLevel(level)
        self.fh.setFormatter(self.formatter)
        self.my_logger.addHandler(self.fh)
        if level == 'DEBUG':
            self.my_logger.debug(msg)
        elif level == 'INFO':
            self.my_logger.error(msg)
        elif level == 'WARNING':
            self.my_logger.warning(msg)
        elif level == 'ERROR':
            self.my_logger.error(msg)
        elif level == 'CRITICAL':
            self.my_logger.critical(msg)
        else:
            return '日志等级不对，请重新输入'
        self.my_logger.removeHandler(self.fh)


if __name__ == '__main__':
    MyLog().my_log('hhhh','ESDAS')
