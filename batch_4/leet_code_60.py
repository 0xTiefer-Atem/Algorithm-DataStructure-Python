"""
排列序列
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。


示例 1：
输入：n = 3, k = 3
输出："213"


示例 2：
输入：n = 4, k = 9
输出："2314"


示例 3：
输入：n = 3, k = 1
输出："123"
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.res = [[]]
        check = [0 for i in range(n)]
        nums = [i for i in range(1, n+1)]
        sol = []
        self.traceback(nums, sol, check)

        res_array = self.res[k]
        res = ""
        for i in range(len(res_array)):
            res += str(res_array[i])

        return str(res)



    def traceback(self, nums, sol, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            check[i] = 1
            self.traceback(nums, sol + [nums[i]], check)
            check[i] = 0



if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(9, 219601))