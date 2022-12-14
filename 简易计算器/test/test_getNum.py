import unittest
from src import main
from tkinter import Tk
from unittestreport import TestRunner
import os

"""
如果getNum没有返回值，但是我们可以通过最后结果值来看这个答案是否正确，给getNum再设置一个参数就可以了
"""


class TestgetNum(unittest.TestCase):

    def test_getNum(self):
        lis_ex = ['e*(10', '7/(49851-20.36', 'exp(0', '/exp(e*π', 'log', '8349/*521', 'e+60821', 'e+125', '2.18043-/',
                  '219', '46017-/2', 'π+', '4-583/10.6*(e', 'π+87.9/36', 'exp(log(9.7/361+π-', '843+', '7*392/-e',
                  '7*392/-e', 'e+log(/π*87526', '28/', '/e-(4+log(9', 'π*/log(385246', '0-', 'exp(19', 'exp(8073/-51',
                  '0.9*(e)-846', 'π/(79', '3.975+/0', '915/e+7438', '17/8-9.', 'π*log(7/)', '0-4/57*exp(', '/(853+e',
                  'π/-7*exp(32.4', '0.479', '946', '1-', 'log(exp(e/(10-8.4573', '0.1*exp(24+3/56', '6805/1.97+',
                  '6805/1.97+', '0*log((713', '4107/e', '12956/4-π+3*8.', '(2-', 'exp(π-3', '/6-439.57', '34-e',
                  'log(exp(72./-', '1348*69+', 'log(e*/(507.48+', '1.506-e/(48*2', '42051793', '86', '468-/521+9.37',
                  '31205*78+exp((log(6/4.', '8-(9+536/014', 'exp(172-3+/60594.', '1+39.524-8*exp(6/e', '248+3/π',
                  '84-/.597+log(6)*1', 'e+(0', '0-(7/)+1*6384', '0.6', 'exp(/4)-π', '0*2.679108+(/54',
                  '4-96175/+exp(8)', '975.0+1*3/684-', '12708-exp(6/+534', 'π', '362+1/.89-0', '362+1/.89-0', '4+0',
                  '0-4', '0*', '5-0/319', '91740*e-π', '1584/', 'π/73*894-e', '(71*e', '0+e-(log(3', '78.0-', '6',
                  '0.214', '0+log(31', '1/', 'log((9', '34/', '/+2578', 'exp(8-4502*936', 'π', '92.7', '42+e/1.509*π-',
                  '5*6-1.2/3890+', '5*6-1.2/3890+', '1.', '0*65', '2*98+log(65/410', 'exp(7-4/08.9+3612*5', '0-5/67']
        lis_all = [['e', 'π', 'log', '2', '9', '.', '*', '(', '1', '0'],
                   ['7', '/', '(', '4', '9', '8', '5', 'log', '1', 'exp', 'π', '-', ')', '2', '0', '.', 'e', '*', '3',
                    '6'], ['exp', '0', '8', '-', '3'], ['/', 'exp', 'e', '*', 'π', '8'], [')', 'log'],
                   ['8', '3', '4', ')', '(', '9', '/', '*', '5', '2', 'exp', '1'],
                   ['e', '+', '.', ')', '6', '0', '8', 'log', 'π', 'exp', '2', '1'],
                   ['e', '9', 'π', '7', '0', '4', '(', '3', '+', '1', '2', ')', '5'],
                   ['2', '.', '+', '1', '8', '0', '4', '3', '-', '/'], ['2', '1', 'π', '9'],
                   ['4', ')', '6', 'log', '0', 'e', '1', '7', '(', '-', '+', '*', '/', '2'],
                   ['π', 'e', 'log', '(', '1', '+'],
                   ['4', '-', '5', '8', '3', '/', '1', '0', '.', ')', '+', '6', '*', '(', 'e', '9', '7', 'π', 'log',
                    'exp', '2'], ['π', 'e', '4', '+', '8', '7', '.', '-', ')', 'exp', '9', '/', '3', '6', 'log'],
                   ['exp', 'log', '9', '.', '7', '/', '3', 'e', '6', '1', '+', ')', 'π', '4', '8', '5', '(', '0', '2',
                    '-'], ['8', '4', 'e', 'exp', ')', '3', '+'],
                   ['7', '*', '3', '9', '2', '/', ')', '-', 'e', 'exp', '8', '0', 'log', 'π', '(', '1', '.'], [],
                   ['e', '3', '1', 'exp', '9', ')', '.', '0', '+', 'log', '-', '/', 'π', '4', '*', '8', '7', '(', '5',
                    '2', '6'], ['2', '8', '/'], ['/', 'e', '-', '(', '4', '+', 'log', '9'],
                   ['π', '7', '*', '/', 'log', '3', '8', '5', '2', '4', '(', '6', 'exp'], ['-', '.'], ['exp', '1', '9'],
                   [')', 'exp', '+', '8', '0', '7', '3', 'π', '(', 'log', '/', '-', '5', '1'],
                   ['.', '9', '*', '(', 'e', '2', ')', '0', '1', '-', '8', '4', '6', 'log'],
                   ['π', '/', '(', '+', '7', '9', 'log'], ['3', '.', 'π', '9', '7', 'e', '5', '+', '*', '/', '0'],
                   ['9', '1', '5', '/', 'e', '2', '+', '7', '4', ')', 'log', 'π', '3', '8'],
                   ['1', '7', '/', '8', '-', '*', '0', '9', 'e', '.'], ['π', '0', '*', 'log', '-', '7', '/', ')'],
                   ['-', '.', ')', '4', '(', '/', '5', '7', '*', 'exp', '+'],
                   ['/', '(', '8', '5', '3', '+', 'e', 'π', '4'],
                   ['π', '6', '0', '5', '/', '-', '7', '*', ')', 'exp', '3', '2', '.', '(', '4', 'e'],
                   ['.', '4', '7', '9', 'exp', 'log'], ['9', '4', '6', 'π', 'log'], ['1', '-', '+'],
                   ['log', 'exp', ')', 'e', '/', '(', '1', 'π', '0', '-', '8', '.', '4', '5', '7', '3'],
                   ['.', '1', ')', 'log', '*', 'exp', '2', '4', '+', '0', '3', '/', '5', '6', 'e', 'π'],
                   ['6', '8', '0', 'e', '5', '/', '1', 'exp', 'π', '.', '9', '7', '+', '-'], [],
                   ['0', '*', 'log', '(', '7', '1', '3'], ['4', '1', '0', '(', '7', '/', 'e'],
                   ['1', 'exp', 'e', '2', '9', '5', '6', '/', '4', '-', 'π', '7', '(', '+', '3', '*', ')', '0', 'log',
                    '8', '.'], ['(', '.', '2', '-'], ['exp', 'π', 'log', '0', '2', '8', '-', '3', '('],
                   ['/', '6', '-', '+', '*', '4', '(', ')', '3', '9', 'π', '.', 'e', '5', '7'], ['3', '4', '-', 'e'],
                   ['log', 'exp', ')', '7', '2', '.', 'π', 'e', '/', '-', '*'],
                   ['1', '3', '4', 'π', '(', '8', '*', ')', '-', '.', '0', 'exp', '6', '9', '+'],
                   ['log', 'e', '*', '/', '(', '5', '0', 'exp', '7', 'π', '.', '-', '4', '8', '+'],
                   ['1', '.', '5', 'exp', '0', '6', '-', 'e', '3', '/', '(', '4', '8', 'log', '*', '2'],
                   ['4', 'e', '2', '0', '5', '1', '7', '9', 'log', '3'], ['8', ')', '6'],
                   ['4', '6', '8', '(', 'log', '-', '/', '5', '2', '1', '+', '0', '9', '.', 'exp', '*', 'e', '3', '7',
                    'π'],
                   ['3', '1', '2', '0', '5', '*', ')', '7', '8', '+', 'exp', '-', '(', 'log', '6', '/', '4', '.', 'e'],
                   ['8', 'e', '-', '(', '9', '+', '5', '3', '6', 'exp', '/', '0', 'π', '1', '4'],
                   ['exp', '1', '7', 'e', '2', '-', '3', '+', '/', '6', '0', 'π', 'log', '(', '5', '9', '4', '.', ')'],
                   ['1', 'log', '+', '3', '9', ')', '.', '5', '2', '4', '(', '-', '0', '8', '*', 'exp', '6', '/', 'e',
                    'π'], ['2', '4', '8', 'log', '+', '*', '0', '3', '(', 'e', '/', ')', 'π'],
                   ['8', '4', 'e', '-', '/', '.', '5', '(', 'exp', 'π', '9', '7', '+', 'log', '6', ')', '2', '0', '3',
                    '*', '1'], ['e', '1', '3', 'log', '2', '6', '9', '8', '+', '(', '.', '0', '-', '*'],
                   ['-', '(', '7', '/', ')', 'exp', 'e', '0', '+', '1', '*', '6', '3', '8', 'π', '4'], ['.', '6', '('],
                   ['exp', '/', '4', ')', '9', '-', 'π'],
                   ['*', '2', '.', 'log', 'e', '6', '7', '9', '1', '0', '8', ')', 'exp', '+', '-', '(', '/', '5', '4'],
                   ['4', '-', '9', '6', '1', '7', 'log', 'e', '5', '/', '+', 'exp', '8', 'π', ')', '3'],
                   ['9', 'exp', 'log', 'π', '(', '7', '5', '.', '0', ')', '+', '1', '*', '3', 'e', '/', '6', '8', '4',
                    '-'],
                   ['1', ')', '2', 'π', '7', '0', '(', 'log', '8', '-', 'exp', '6', '/', '+', '.', '5', '3', 'e', '4'],
                   ['π', '8', '.', ')', '3', '2'],
                   ['3', '6', '2', '+', '*', '1', 'exp', '/', '.', '8', 'log', '9', '-', '0'], [], ['4', '+', '0'],
                   ['-', '4'], ['*'], ['5', '-', '.', '0', '/', '3', 'e', '1', '9'],
                   ['9', ')', '1', '7', '4', '0', '*', 'e', '-', '.', 'π'], ['1', 'log', '5', '8', '4', '/'],
                   ['π', '/', ')', '7', '3', '*', '0', '8', 'exp', '9', '4', '-', '+', 'e', '5', '6', '1', '(', '.',
                    'log'], ['(', '7', '1', '*', 'e'], ['+', 'e', '-', '(', 'log', '3'],
                   ['7', 'exp', '8', '.', '0', '-', ')'], ['6'], ['.', '-', '2', '1', '4'], ['+', ')', 'log', '3', '1'],
                   ['1', '/'], ['log', '(', '9', 'π', 'e'], ['3', '4', '/'], ['/', '+', '2', '(', '5', '7', 'π', '8'],
                   ['exp', '8', 'π', '-', '4', 'e', '5', '0', '2', '*', '9', '3', '6'], [')', 'π', '('],
                   ['9', '2', 'e', '.', '(', '7'],
                   ['4', '2', '+', 'e', '(', '6', '/', '1', '.', '5', '0', '9', 'log', 'exp', '*', 'π', '3', ')', '7',
                    '-'], ['5', '*', '6', 'π', '-', '1', 'log', '.', '2', '/', '3', '(', '8', '9', '0', '+'], [],
                   ['1', '.', '+', ')', 'e'], ['*', '+', '.', '0', 'exp', '(', '6', '5'],
                   ['2', ')', '*', '9', '8', '+', '-', 'log', '6', '5', 'exp', 'e', '/', '4', '1', '0'],
                   ['exp', '7', '(', '-', '4', 'π', '/', '0', '8', '.', 'e', ')', '9', '+', '3', '6', '1', '2', 'log',
                    '*', '5'], ['-', '*', '5', 'log', '/', '6', 'π', '7']]
        root = Tk()
        my_cal = main.Calculator(root)
        for j in range(len(lis_all)):
            lis = lis_all[j]
            for i in lis:
                my_cal.getNum(i)
            self.assertEqual(lis_ex[j], my_cal.getNum_help)
            main.b = True


suite = unittest.TestSuite()
suite.addTest(TestgetNum("test_getNum"))

BasePath = os.path.dirname(__file__)  # 获取当前文件所在路径
if __name__ == '__main__':
    fp = BasePath
    runner = TestRunner(suite, filename="test_getNum_report.html",
                        report_dir=r'..\test\htmlcov', title="测试报告",
                        tester="LLEI", desc="LLEI执行的测试用例")
    runner.run()
