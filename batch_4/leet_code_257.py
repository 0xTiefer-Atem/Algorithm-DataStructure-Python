"""
二叉树的所有路径

给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明:叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.preOrder(root, "")
        return self.res


    def preOrder(self, root: TreeNode, path: List):
        if root:
            if root.left or root.right:
                path += str(root.val) + "->"
                if root.left:
                    self.preOrder(root.left, path)
                if root.right:
                    self.preOrder(root.right, path)
            else:
                path += str(root.val)
                self.res.append(path)



if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.right = node5

    s = Solution()

    print(s.binaryTreePaths(node1))