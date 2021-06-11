"""
矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

示例 1：

输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]


示例 2：


输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        locate_dict = {}

        row_num = len(matrix)
        clo_num = len(matrix[0])

        count = 1
        for i in range(row_num):
            for j in range(clo_num):
                if matrix[i][j] == 0:
                    locate_dict['index' + str(count)] = [i, j]
                    count += 1

        for key, val in locate_dict.items():
            row, clo = val

            for i in range(clo_num):
                matrix[row][i] = 0

            for j in range(row_num):
                matrix[j][clo] = 0


if __name__ == '__main__':
    s = Solution()
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(matrix)
