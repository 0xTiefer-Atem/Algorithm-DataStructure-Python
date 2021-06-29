"""
全排列 II

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]


示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]
        self.traceback(nums, check, [])

        return self.res

    def traceback(self, nums, check, sol):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue

            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 1:
                continue

            check[i] = 1
            self.traceback(nums, check, sol + [nums[i]])
            check[i] = 0


if __name__ == '__main__':
    nums = [3, 3, 0, 3]
    s = Solution()
    print(s.permuteUnique(nums))
