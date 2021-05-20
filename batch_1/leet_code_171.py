"""
给定一个Excel表格中的列名称，返回其相应的列序号
例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...


示例 1:

输入: "A"
输出: 1


示例 2:

输入: "AB"
输出: 28


示例 3:

输入: "ZY"
输出: 701

"""
from builtins import str


class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber:
            columnNumber -= 1
            s = chr(columnNumber % 26 + 65) + s
            columnNumber = columnNumber // 26
        return s


    def titleToNumber(self, columnTitle: str) -> int:

        length = len(columnTitle) - 1
        index = 0
        res = 0
        while length >= 0:
            res += 26**length * (ord(columnTitle[index]) - ord('A') + 1)
            length -= 1
            index += 1

        return res



if __name__ == '__main__':
    s = Solution()
    str = s.convertToTitle(52)

    print(s.titleToNumber(str))