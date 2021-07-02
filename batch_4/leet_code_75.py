"""
颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]


示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]


示例 3：
输入：nums = [0]
输出：[0]


示例 4：
输入：nums = [1]
输出：[1]
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                temp = nums[i]
                j = i - 1
                while j >= 0 and temp < nums[j]:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = temp


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]

    s = Solution()
    s.sortColors(nums)
