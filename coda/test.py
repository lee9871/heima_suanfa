# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        # 考虑当前root,递归删除root.left 和 root.right中的target。
        # 接着判断root是不是要删除的点，如果是，并且左节点和右节点 也为空的话，直接删除返回空
        # 否则，返回root

        def recur(root):
            if not root:
                return None
            root.left = recur(root.left)
            root.right = recur(root.right)
            if not root.left and not root.right and root.val == target:
                return None
            return root

        return recur(root)

a = Solution()
a.removeLeafNodes(root = [1,2,3,2,None,2,4], target =2)