# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Attempt 3: Neetcode's iterative solution (viewed code): https://www.youtube.com/watch?v=5LUXSvjmGCw
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        cur = root
        stack = []
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right
