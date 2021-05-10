"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：

输入：x = 123
输出：321


示例 2：

输入：x = -123
输出：-321


示例 3：

输入：x = 120
输出：21


示例 4：

输入：x = 0
输出：0


"""


class Solution:
    def reverse(self, x: int) -> int:
        number_str = str(x)

        if x == 0:
            return 0

        # 负号标志
        flag = False
        if number_str[0] == '-':
            number_str = number_str[1:]
            flag = True


        number_len = len(number_str)

        re_number_str = ''
        for i in range(number_len - 1, -1, -1):
            re_number_str += number_str[i]

        if flag:
            re_number_str = '-' + re_number_str

        re_number = int(re_number_str)

        if -2 ** 31 <= re_number <= 2 ** 31 - 1:
            return re_number

        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-120))
