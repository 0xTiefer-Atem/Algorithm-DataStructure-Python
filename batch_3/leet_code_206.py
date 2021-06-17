"""
反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]


示例 2：

输入：head = [1,2]
输出：[2,1]


示例 3：

输入：head = []
输出：[]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp_head = ListNode()

        while head:
            p = head.next
            head.next = temp_head.next
            temp_head.next = head
            head = p

        return temp_head.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    res = s.reverseList(node1)

    while res:
        print(res.val, end=' ')
        res = res.next
