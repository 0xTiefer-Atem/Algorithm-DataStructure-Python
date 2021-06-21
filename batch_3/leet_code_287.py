"""
寻找重复数

给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

示例 1：

输入：nums = [1,3,4,2,2]
输出：2


示例 2：

输入：nums = [3,1,3,4,2]
输出：3


示例 3：

输入：nums = [1,1]
输出：1


示例 4：

输入：nums = [1,1,2]
输出：1

"""
from typing import List
import time


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_dict = dict()

        for i in range(len(nums)):
            if num_dict.__contains__(str(nums[i])):
                return nums[i]
            num_dict[str(nums[i])] = 1


if __name__ == '__main__':
    nums = [3, 1, 3, 4, 2]
    s = Solution()
    # print(s.findDuplicate(nums))

    for i in range(10):

        print('\r{}'.format(i), end="")
        time.sleep(.5)
