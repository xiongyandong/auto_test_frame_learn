import unittest
from TestCase.p2p.test_ddtFromExcel import TestHttp
suite = unittest.TestSuite()
loader = unittest.TestLoader()


class TestSuit:
    def __init__(self, suite_object=suite, loader_object=loader):
        self.suite = suite_object
        self.loader = loader_object

    def make_suite_by_loader(self):
        self.suite.addTest(loader.loadTestsFromTestCase(TestHttp))
        return self.suite

    def make_suite_by_case(self):
        pass


if __name__ == '__main__':
    t = TestSuit(suite, loader).make_suite_by_loader()
    print(t)
