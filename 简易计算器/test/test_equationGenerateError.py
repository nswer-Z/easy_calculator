import unittest
from src.main import testEquationGenerateError


class TestEquGerError(unittest.TestCase):
    """ 结果标签为空

    输入新的计算式子，在按下'='前，没有结果，结果显示区域应该为空

    """
    def test_resultDisplay(self):
        self.temp_equ = '2+3*'
        self.arg = '5'
        self.test_result = 'random'
        self.temp_result = self.test_result
        arg, temp_equ_new, test_result = testEquationGenerateError(self.arg, self.temp_equ, self.temp_result,
                                                                   self.test_result)
        temp_equ_new += arg
        assert test_result == ' '
        assert temp_equ_new == '2+3*5'
    """ 小数测试

    输入小数时其只能有一个小数点，输第二个时变为''不显示

    """

    def test_dot(self):
        self.temp_equ = ['0', '0.', '0.1']
        self.arg = '.'
        self.test_result = 'random'
        self.temp_result = self.test_result
        equ = []
        i = 0
        while i < len(self.temp_equ):
            arg, temp_equ_new, test_result = testEquationGenerateError(self.arg, self.temp_equ[i], self.temp_result,
                                                                       self.test_result)
            temp_equ_new += arg
            equ.append(temp_equ_new)
            i += 1
        assert equ == ['0.', '0.', '0.1']

    """ 括号测试
    
    左括号的左边只能是左括号和加减乘除，右边只能是左括号和数字、exp、log
    
    右括号左边只能是右括号和数字，右边只能是右括号和加减乘除
    
    输入右括号是，右括号的数量小于左括号且不能与左括号相邻
    
    """

    def test_brackets(self):
        # 输入右括号是，右括号的数量小于左括号且不能与左括号相邻
        self.arg0 = ')'
        self.temp_equ0 = ['(0', '2', '((3', '(', '(2+5', 'e', '((5+9)+9']
        # 左括号左边测试
        self.arg1 = '('
        self.temp_equ1 = ['0.', '2', '3+', '(', ')', 'e', '*']
        # 右括号左边测试
        self.arg2 = ')'
        self.temp_equ2 = ['(0.', '(2', '(3+', '(', '((1)', '(e', '(4*']
        # 左括号右边测试
        self.arg3 = [')', '0', 'e', '+', '.', '(']
        self.temp_equ3 = '('
        # 右括号右边测试
        self.arg4 = [')', '0', '*', '+', '.', '(']
        self.temp_equ4 = '((0)'
        self.test_result = 'random'
        self.temp_result = self.test_result
        equ0 = []
        equ1 = []
        equ2 = []
        equ3 = []
        equ4 = []
        i = 0
        while i < len(self.temp_equ0):
            arg, temp_equ_new0, test_result = testEquationGenerateError(self.arg0, self.temp_equ0[i], self.temp_result,
                                                                        self.test_result)
            temp_equ_new0 += arg
            equ0.append(temp_equ_new0)

            arg, temp_equ_new1, test_result = testEquationGenerateError(self.arg1, self.temp_equ1[i], self.temp_result,
                                                                        self.test_result)
            temp_equ_new1 += arg
            equ1.append(temp_equ_new1)

            arg, temp_equ_new2, test_result = testEquationGenerateError(self.arg2, self.temp_equ2[i], self.temp_result,
                                                                        self.test_result)
            temp_equ_new2 += arg
            equ2.append(temp_equ_new2)
            i += 1

        assert equ0 == ['(0)', '2', '((3)', '(', '(2+5)', 'e', '((5+9)+9)']
        assert equ1 == ['0.', '2', '3+(', '((', ')', 'e', '*(']
        assert equ2 == ['(0.', '(2)', '(3+', '(', '((1))', '(e)', '(4*']
        i = 0
        while i < len(self.arg3):
            arg, temp_equ_new3, test_result = testEquationGenerateError(self.arg3[i], self.temp_equ3, self.temp_result,
                                                                        self.test_result)
            temp_equ_new3 += arg
            equ3.append(temp_equ_new3)
            arg, temp_equ_new4, test_result = testEquationGenerateError(self.arg4[i], self.temp_equ4, self.temp_result,
                                                                        self.test_result)
            temp_equ_new4 += arg
            equ4.append(temp_equ_new4)
            i += 1
        assert equ3 == ['(', '(0', '(e', '(', '(', '((']
        assert equ4 == ['((0))', '((0)', '((0)*', '((0)+', '((0)', '((0)']

    """ 第一个输入测试
    
    有两种情况：
    
    :表达式为''
    :表达式为'0'
    
    """

    def test_firstInput(self):
        self.temp_equ1 = ''
        self.temp_equ2 = '0'
        self.arg = ['+', '0', '2', '.', 'log', '(', ')', 'e']
        self.test_result = 'random'
        self.temp_result = self.test_result
        equ1 = []
        equ2 = []
        i = 0
        while i < len(self.arg):
            arg, temp_equ_new1, test_result = testEquationGenerateError(self.arg[i], self.temp_equ1, self.temp_result,
                                                                        self.test_result)
            temp_equ_new1 += arg
            equ1.append(temp_equ_new1)
            arg, temp_equ_new2, test_result = testEquationGenerateError(self.arg[i], self.temp_equ2, self.temp_result,
                                                                        self.test_result)
            temp_equ_new2 += arg
            equ2.append(temp_equ_new2)
            i += 1
        assert equ1 == ['', '0', '2', '', 'log', '(', '', 'e']
        assert equ2 == ['0+', '0', '2', '0.', 'log', '(', '', 'e']

    """ 不支持点乘
    
    即字母、数字、左括号左边、右括号右边之间不能无符号相连
    
    """

    def test_dotProduct(self):
        self.temp_equ = ['2', 'e', '(6+5)']
        self.arg = ['2', 'e', '(', 'log', '+', '.']
        self.test_result = 'random'
        self.temp_result = self.test_result
        equ1 = []
        equ2 = []
        equ3 = []
        i = 0
        while i < len(self.temp_equ):
            k = 0
            while k < len(self.arg):
                arg, temp_equ_new, test_result = testEquationGenerateError(self.arg[k], self.temp_equ[i],
                                                                           self.temp_result, self.test_result)
                temp_equ_new += arg
                if i == 0:
                    equ1.append(temp_equ_new)
                elif i == 1:
                    equ2.append(temp_equ_new)
                elif i == 2:
                    equ3.append(temp_equ_new)
                k += 1
            i += 1
        assert equ1 == ['22', '2', '2', '2', '2+', '2.']
        assert equ2 == ['e', 'e', 'e', 'e', 'e+', 'e']
        assert equ3 == ['(6+5)', '(6+5)', '(6+5)', '(6+5)', '(6+5)+', '(6+5)']


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
