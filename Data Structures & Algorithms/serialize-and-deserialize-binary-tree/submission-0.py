# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        msg = ""
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node:
                msg += str(node.val) + " "
                q.append(node.left)
                q.append(node.right)
            else: 
                msg += "n "
            
        print(msg)
        return msg

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        i = 0
        val = ""
        while data[i] != " ":
                val += data[i]
                i += 1
        root = TreeNode(int(val))
        q = deque()
        q.append(root)
        

        while q:
            if data[i] == " ":
                i += 1
                continue

            left_val = ""
            while data[i] != " ":
                left_val += data[i]
                i += 1
            
            i += 1
            right_val = ""
            while data[i] != " ":
                right_val += data[i]
                i += 1
            
            node = q.popleft()
            
            if left_val != "n":
                node.left = TreeNode(int(left_val))
                q.append(node.left)
            if right_val != "n":
                node.right = TreeNode(int(right_val))  
                q.append(node.right)
        return root
