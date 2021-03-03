# --*-- coding : utf-8 --*--
# @Time: 2021/2/19 10:26
# @User: root
# @IDE: PyCharm
# @Author : xyd_boss
# @File: perform_suit.py
import unittest

suite = unittest.TestSuite()
loader = unittest.TestLoader()


class SaaSwebsiteSuit:
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    def make_suite_by_loader(self, _class):
        self.suite.addTest(loader.loadTestsFromTestCase(_class))
        return self.suite

    def make_suite_by_case(self):
        pass


if __name__ == '__main__':
    pass

