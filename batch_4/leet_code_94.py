"""
二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]


示例 2：
输入：root = []
输出：[]


示例 3：
输入：root = [1]
输出：[1]


示例 4：
输入：root = [1,2]
输出：[2,1]


示例 5：
输入：root = [1,null,2]
输出：[1,2]
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.orderlist = []
        self.inorder(root)
        return self.orderlist


    def inorder(self, root: TreeNode):
        if root:
            self.inorder(root.left)
            self.orderlist.append(root.val)
            self.inorder(root.right)


if __name__ == '__main__':
    node1 = TreeNode(1)

    node2 = TreeNode(2)

    node1.left = node2

    s = Solution()

    print(s.inorderTraversal(node1))
