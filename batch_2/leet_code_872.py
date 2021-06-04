"""
叶子相似的树

请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。


示例 1：

输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true


示例 2：

输入：root1 = [1], root2 = [1]
输出：true


示例 3：

输入：root1 = [1], root2 = [2]
输出：false


示例 4：

输入：root1 = [1,2], root2 = [2,2]
输出：true


示例 5：

输入：root1 = [1,2,3], root2 = [1,3,2]
输出：false

"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root1_node_list = []
        self.root2_node_list = []

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.preorder(root1, self.root1_node_list)
        self.preorder(root2, self.root2_node_list)

        print(self.root1_node_list)
        print(self.root2_node_list)

        if len(self.root1_node_list) != len(self.root2_node_list):
            return False

        for i in range(min(len(self.root1_node_list), len(self.root2_node_list))):
            if self.root1_node_list[i] != self.root2_node_list[i]:
                return False

        return True

    def preorder(self, root: TreeNode, node_list: List) -> None:
        if root:
            self.preorder(root.left, node_list)
            if root.left is None and root.right is None:
                node_list.append(root.val)
            self.preorder(root.right, node_list)


if __name__ == '__main__':
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node3.left = node5
    node3.right = node1

    node5.left = node6
    node5.right = node2

    node2.left = node7
    node2.right = node4

    node1.left = node9
    node1.right = node8

    print(s.leafSimilar(node9, node9))
