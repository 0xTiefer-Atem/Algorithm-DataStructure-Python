"""
119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        out_layer = list()

        for i in range(rowIndex + 1):
            in_layer = list()
            in_layer.append(1)
            for j in range(i):
                if j == i - 1:
                    in_layer.append(1)
                else:
                    in_layer.append((out_layer[i - 1][j] + out_layer[i - 1][j + 1]))
            # print(i, ' ' * (rowIndex - i), in_layer)
            out_layer.append(in_layer)

        return out_layer[rowIndex]


if __name__ == '__main__':
    solution = Solution()

    numRows = 33
    res = solution.getRow(numRows)
    print(res)