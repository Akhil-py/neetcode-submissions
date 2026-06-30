"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        
        visited = set()
        newNodeMap = {}
        q = collections.deque()
        newQ = collections.deque()
        newNode = Node(1)
        newCurr = newNode
        newNodeMap[newNode.val] = newNode

        q.append(node)
        while q:
            curr = q.popleft()
            neighbors = []
            for i in curr.neighbors:
                if i.val in newNodeMap:
                    nextNode = newNodeMap[i.val]
                else:
                    nextNode = Node(i.val)
                    newNodeMap[i.val] = nextNode
                neighbors.append(nextNode)
                if i.val not in visited:
                    q.append(i)
                    newQ.append(nextNode)
            newCurr.neighbors = neighbors

            visited.add(curr.val)
            if newQ:
                newCurr = newQ.popleft()


        return newNode
            