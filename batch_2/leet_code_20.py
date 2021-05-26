"""
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        valid_list = []

        for i in range(len(s)):
            lenght = len(valid_list)
            if lenght == 0:
                valid_list.append(s[i])
            else:
                char = valid_list[lenght-1]
                if str(char + s[i]) == "()" or str(char + s[i]) == "[]" or str(char + s[i]) == "{}":
                    valid_list.pop(lenght-1)
                else:
                    valid_list.append(s[i])


        return len(valid_list) == 0




if __name__ == '__main__':
    s = Solution()

    print(s.isValid('({[)'))