class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighborMap = { i : [] for i in range(n) }
        for i, j in edges:
            neighborMap[i].append(j)
            neighborMap[j].append(i)

        visited = set()
        seen = set()
        def dfs(prev, curr):
            if curr in visited:
                return False
            visited.add(curr)
            seen.add(curr)
            for neighbor in neighborMap[curr]:
                if neighbor != prev:
                    if not dfs(curr, neighbor): return False
            visited.remove(curr)

            return True
        
        isTree = dfs(-1, 0)
        for i in neighborMap:
            if i not in seen:
                return False
        return isTree