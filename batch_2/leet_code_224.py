"""
基本计算器
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3+6+8)"
输出：23

"""


class Solution:
    def calculate(self, expression: str) -> int:
        expression = expression.replace(" ", "")
        res = 0
        expression_list = []
        for i in range(len(expression)):
            if expression[i] == ")":
                temp_left_bracket = 0
                expression_list_len = len(expression_list)
                for j in range(expression_list_len - 1, -1, -1):
                    if expression_list[j] == "(":
                        res = self.calculate_subexpression(expression_list[j + 1:])
                        expression_list[j] = str(res)
                        expression_list = expression_list[:j+1]

            else:
                expression_list.append(expression[i])


        return self.calculate_subexpression(expression_list)

    def calculate_subexpression(self, subexpression_list):
        print(subexpression_list)
        temp_res = int(subexpression_list[0])
        for i in range(1, len(subexpression_list)):
            if subexpression_list[i] == "+":
                temp_res = self.add(temp_res, int(subexpression_list[i + 1]))
            elif subexpression_list[i] == "-":
                temp_res = self.sub(temp_res, int(subexpression_list[i + 1]))

        # print("subexpression_list: {}, temp_res: {}".format(subexpression_list, temp_res))
        return temp_res

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y




if __name__ == '__main__':
    expression = "+48 + -48"
    s = Solution()

    # subexpression_list = ['4', '+', '5', '+', '2']
    # print(s.calculate_subexpression(subexpression_list))
    # res = s.calculate(expression)
    print(eval(expression))
