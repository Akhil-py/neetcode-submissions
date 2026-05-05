# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if node.val < left or node.val> right:
                return False
            if node.left and node.right:
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)

            if node.left:
                return valid(node.left, left, node.val)
            
            if node.right:
                return valid(node.right, node.val, right)

            if left < node.val < right:
                return True
            else:
                return False

        left = -10000
        right = 10000

        return valid(root, left, right)

            