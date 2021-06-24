"""
排序数组

给你一个整数数组 nums，请你将该数组升序排列。

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]


示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    # def sort(self, nums: List[int], low, high):
    #     if low < high:
    #         pos = self.quickSort(nums, low, high)
    #         self.sort(nums, low, pos - 1)
    #         self.sort(nums, pos, high)
    #
    # def quickSort(self, nums: List[int], low, high) -> int:
    #     key = nums[low]
    #     while low < high:
    #         while low < high and nums[high] >= key:
    #             high -= 1
    #         nums[low] = nums[high]
    #
    #         while low < high and nums[low] <= key:
    #             low += 1
    #         nums[high] = nums[low]
    #
    #     nums[low] = key
    #
    #     return high

    def quick_sort(self, alist, start, end):
        """快速排序"""
        if start >= end:  # 递归的退出条件
            return
        mid = alist[start]  # 设定起始的基准元素
        low = start  # low为序列左边在开始位置的由左向右移动的游标
        high = end  # high为序列右边末尾位置的由右向左移动的游标
        while low < high:
            # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
            while low < high and alist[high] >= mid:
                high -= 1
            alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
            # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
            while low < high and alist[low] < mid:
                low += 1
            alist[high] = alist[
                low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

        # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
        alist[low] = mid  # 将基准元素放到该位置,
        # 对基准元素左边的子序列进行快速排序
        self.quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
        # 对基准元素右边的子序列进行快速排序
        self.quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后


if __name__ == '__main__':
    nums = [5, 2, 3, 1]

    s = Solution()

    print(s.sortArray(nums))
