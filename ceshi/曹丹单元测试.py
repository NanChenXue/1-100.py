import unittest
from 曹丹单元测试代码 import CheckEvenOdd
class Test_is1(unittest.TestCase):
    def setUp(self):
        print("测试开始")
    def testcheckEvenOdd(self):
        # c=int(CheckEvenOdd(2));
        # self.assertEqual(1,c)
        self.assertEqual(1,CheckEvenOdd(2))
    def tearDown(self):
        print("测试结束")