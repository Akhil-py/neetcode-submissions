# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            # Max with split
            max_sum = max(left, 0) + max(right, 0) + root.val

            if max_sum > res[0]:
                res[0] = max_sum
            
            # Max without split
            return max(left, right, 0) + root.val

        dfs(root)
        return res[0]