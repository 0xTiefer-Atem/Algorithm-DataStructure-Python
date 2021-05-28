"""
对链表进行插入排序。

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。


示例 1：

输入: 4->2->1->3
输出: 1->2->3->4


示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5


"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return ListNode()

        tempHead = ListNode()
        tempHead.next = head

        cur = head

        while cur.next:
            if cur.val > cur.next.val:
                move_ptr = cur.next
                temp = tempHead
                while temp.next.val < move_ptr.val:
                    temp = temp.next
                cur.next = move_ptr.next
                move_ptr.next = temp.next
                temp.next = move_ptr

            else:
                cur = cur.next

        return tempHead.next


if __name__ == '__main__':
    n1 = ListNode(-1)

    n2 = ListNode(5)
    n1.next = n2

    n3 = ListNode(3)
    n2.next = n3

    n4 = ListNode(4)
    n3.next = n4

    n5 = ListNode(0)
    n4.next = n5

    n6 = ListNode(2)
    n5.next = n6

    s = Solution()
    res = s.insertionSortList(n1)
    while res:
        print(res.val, end=' ')
        res = res.next
