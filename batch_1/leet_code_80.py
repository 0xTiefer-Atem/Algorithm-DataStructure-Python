"""
80. 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # 列表长度
        length = len(nums)

        # 临时保存的变量
        temp = None

        # 元素出现的次数
        dup_nums = 0

        # 记录修改后数组的长度
        new_length = 0
        if len(nums) == 0:
            return new_length

        for i in range(length - 1):
            if temp != nums[i]:
                dup_nums = 0
                temp = nums[i]
                dup_nums += 1
            if nums[i] == nums[i + 1]:
                dup_nums += 1
                if dup_nums > 2:
                    nums[i] = None
        # print(nums)

        for i in range(length):
            if nums[i] is None:
                j = i
                while j < length-1 and nums[j] is None:
                    j += 1
                nums[i] = nums[j]
                nums[j] = None
            # print(i, nums)

        for i in range(length):
            if nums[i] is not None:
                new_length += 1

        return new_length


if __name__ == '__main__':
    nums_1 = [1, 1, 1, 2, 2, 3]
    nums_2 = [0, 0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3]
    nums_3 = [0, 0, 0]
    nums_4 = []
    nums_5 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    solution = Solution()
    length = solution.removeDuplicates(nums_5)
    print(length, nums_5)
