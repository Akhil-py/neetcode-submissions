# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Attempt 2: Neetcode's iterative solution: https://www.youtube.com/watch?v=5LUXSvjmGCw
    # Attempted without looking at code and only watching the logic explanation
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        ordered = []
        stack.append(root)

        while stack:
            node = stack[-1]
            while node.left and node.left.val not in ordered:
                stack.append(node.left)
                node = stack[-1]
            node = stack.pop()
            ordered.append(node.val)
            if node.right:
                stack.append(node.right)
        
        return ordered[k - 1]
