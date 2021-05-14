"""
118. 杨辉三角
给定一个非负整数numRows，生成杨辉三角的前numRows行。


在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out_layer = list()

        for i in range(numRows):
            in_layer = list()
            in_layer.append(1)
            for j in range(i):
                if j == i - 1:
                    in_layer.append(1)
                else:
                    in_layer.append((out_layer[i - 1][j] + out_layer[i - 1][j + 1]))
            print(i, ' ' * (numRows - i), in_layer)
            out_layer.append(in_layer)

        return out_layer


if __name__ == '__main__':
    solution = Solution()

    numRows = 33
    res = solution.generate(numRows)
    # print(res)