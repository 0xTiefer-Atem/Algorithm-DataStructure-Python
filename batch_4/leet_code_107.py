"""
二叉树的层序遍历 II

给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]

        node_list = []
        res_list = []
        temp_res = []
        node_list.append(root)
        level_num = 1
        while len(node_list) > 0:
            node = node_list.pop(0)
            level_num -= 1
            temp_res.append(node.val)

            if node.left:
                node_list.append(node.left)

            if node.right:
                node_list.append(node.right)

            if level_num == 0:
                res_list.append(temp_res)
                level_num = len(node_list)
                temp_res = []

        return [res_list[i] for i in range(len(res_list) - 1, -1, -1)]


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    s = Solution()

    print(s.levelOrderBottom(node1))
