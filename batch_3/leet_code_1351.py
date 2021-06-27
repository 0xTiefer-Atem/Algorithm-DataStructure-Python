"""
统计有序矩阵中的负数

给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。

请你统计并返回 grid 中 负数 的数目。

示例 1：

输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。


示例 2：

输入：grid = [[3,2],[1,0]]
输出：0


示例 3：

输入：grid = [[1,-1],[-1,-1]]
输出：3


示例 4：

输入：grid = [[-1]]
输出：1
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row_num = len(grid)
        negatives_nums = 0

        for i in range(row_num):
            clo_num = len(grid[i])
            for j in range(clo_num):
                if grid[i][j] < 0:
                    negatives_nums += (clo_num - j)
                    break

        return negatives_nums


if __name__ == '__main__':
    grid = [[-1]]

    s = Solution()

    print(s.countNegatives(grid))
