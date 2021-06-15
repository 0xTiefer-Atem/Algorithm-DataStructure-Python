"""
平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。


示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：true


示例 2：

输入：root = [1,2,2,3,3,null,null,4,4]
输出：false


示例 3：

输入：root = []
输出：true
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            if abs(self.countSubTreeDeepth(root.left) - self.countSubTreeDeepth(root.right)) > 1:
                return False
            elif self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False

    def countSubTreeDeepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.countSubTreeDeepth(root.left), self.countSubTreeDeepth(root.right))


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node2.left = node4
    node2.right = node5

    node6 = TreeNode(6)

    node4.left = node6

    node7 = TreeNode(7)

    node3.left = node7

    s = Solution()

    print(s.isBalanced(node1))
