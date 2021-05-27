"""
二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：

输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]


示例 2：

输入：root = []
输出：[]


示例 3：

输入：root = [0]
输出：[0]

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root:
            self.flatten(root.left)

            temp_root = root
            if temp_root.left is not None:
                left_leave = temp_root.left
                right_leave = temp_root.right

                temp_root.left = None

                right_node = left_leave
                while right_node.right is not None:
                    right_node = right_node.right

                temp_root.right = left_leave
                right_node.right = right_leave

            self.flatten(root.right)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node7 = TreeNode(0)

    node1.left = node2
    node1.right = node5

    node2.left = node3
    node2.right = node4

    node5.right = node6



    s = Solution()
    s.flatten(node7)
    print("-----")
