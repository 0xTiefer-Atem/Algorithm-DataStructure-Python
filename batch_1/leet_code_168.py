"""
Excel表列名称
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...


示例 1:

输入: 1
输出: "A"


示例 2:

输入: 28
输出: "AB"


示例 3:

输入: 701
输出: "ZY"

"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber:
            columnNumber -= 1
            s = chr(columnNumber % 26 + 65) + s
            columnNumber = columnNumber // 26
        return s


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(777))
