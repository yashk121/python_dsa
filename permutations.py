# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], llimit=-2 ** 31 + 1, rlimit=2 ** 31 +1) -> bool:
        if root == None:
            return True
        l, r = True, True
        ob = Solution()
        if root.left:

            if root.left.val < root.val and root.left.val > llimit and root.left.val <= rlimit:

                l = ob.isValidBST(root.left, llimit, root.val)
            else:
                return False
        if root.right:
            if root.right.val > root.val and root.right.val > llimit and root.right.val <= rlimit:

                r = ob.isValidBST(root.right, root.val, rlimit)
            else:
                return False
        return l and r


if __name__ == '__main__':
    obj = Solution()
    right = TreeNode(2147483647)
    root = TreeNode(-2147483648, right=right)
    print(obj.isValidBST(root))
