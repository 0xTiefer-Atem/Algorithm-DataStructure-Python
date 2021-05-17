"""
143. 重排链表
    给定一个单链表L：L0→L1→…→Ln-1→Ln ，
    将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

    示例1:
    给定链表 1->2->3->4, 重新排列为 1->4->2->3.

    示例 2:
    给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        num_list = []
        p = head
        while p:
            num_list.append(p.val)
            p = p.next
        print(num_list)

        head = ListNode(num_list[0])
        p = head

        length = len(num_list)

        mid_num = int(length / 2) + 1

        for i in range(1, mid_num):

            new_node_1 = ListNode(num_list[length - i])
            p.next = new_node_1
            p = p.next

            if i == length - i:
                break

            new_node_2 = ListNode(num_list[i])
            p.next = new_node_2
            p = p.next

        print()
        # p = head
        # while p:
        #     print(p.val, end=' ')
        #     p = p.next


if __name__ == '__main__':
    node1 = ListNode(1)

    node2 = ListNode(2)
    node1.next = node2

    node3 = ListNode(3)
    node2.next = node3

    node4 = ListNode(4)
    node3.next = node4

    node5 = ListNode(5)
    node4.next = node5

    solution = Solution()
    solution.reorderList(node1)

    p = node1
    while p:
        print(p.val, end=' ')
        p = p.next
