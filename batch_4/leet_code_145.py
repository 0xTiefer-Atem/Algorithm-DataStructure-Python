"""
二叉树的后序遍历
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.postOrder(root)
        return self.res


    def postOrder(self, root: TreeNode):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            self.res.append(root.val)
        return


if __name__ == '__main__':
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    print(s.postorderTraversal(node1))