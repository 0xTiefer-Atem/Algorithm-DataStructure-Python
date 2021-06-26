"""
二叉树的堂兄弟节点

在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。


示例 1：

输入：root = [1,2,3,4], x = 4, y = 3
输出：false


示例 2：

输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true


示例 3：

输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    parent_root = None
    val_depth = 0


    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        self.findValDepth(root, x)
        self.findParent(root, x)
        x_depth = self.val_depth
        x_parent = self.parent_root

        self.findValDepth(root, y)
        self.findParent(root, y)
        y_depth = self.val_depth
        y_parent = self.parent_root

        print(x_depth, y_depth)
        print(x_parent, y_parent.val)

        return (x_depth == y_depth) and (x_parent is not y_parent)

    # 找出该节点的深度
    def findValDepth(self, root: TreeNode, child_val: int):
        if root:
            if root.val == child_val:
                self.val_depth += 1
        else:
            self.val_depth += 1
            self.findValDepth(root.left, child_val)
            self.findValDepth(root.right, child_val)

    def findParent(self, root: TreeNode, child_val):
        if root:
            if (root.left is not None and root.left.val == child_val) or (
                    root.right is not None and root.right.val == child_val):
                self.parent_root = root
                return
        else:
            self.findParent(root.left, child_val)
            self.findParent(root.right, child_val)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3

    node2.left = node4

    s = Solution()

    print(s.isCousins(node1, 4, 3))
