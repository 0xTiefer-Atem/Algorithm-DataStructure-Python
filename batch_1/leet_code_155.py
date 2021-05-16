"""
155. 最小栈

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        # 正常存储数据
        self.stack = list()

        # 栈中数据个数当作下标
        self.nums = 0

        # 当前栈顶指针
        self.index = -1

        # 从小到大存储数据
        self.mini_list = list()

    def push(self, val: int) -> None:

        if self.index == len(self.stack) - 1:
            # 入栈
            self.stack.append(val)

            # 栈顶指针指向栈顶
            self.index += 1
        else:
            self.index += 1
            self.stack[self.index] = val

        # 存入当前最小的值
        self.mini_list.append(val)

        self.mini_list.sort(reverse=False)


    def pop(self) -> None:

        self.mini_list.remove(self.stack[self.index])

        if self.index >= 0:
            self.index -= 1

    def top(self) -> int:
        return self.stack[self.index]

    def getMin(self) -> int:
        if len(self.mini_list) > 0:
            return self.mini_list[0]

    def getStack(self):
        return self.stack


if __name__ == '__main__':
    miniStack = MinStack()
    miniStack.push(-2)
    miniStack.push(0)
    miniStack.push(-3)

    print(miniStack.getMin())

    miniStack.pop()
    print(miniStack.top())
    print(miniStack.getMin())