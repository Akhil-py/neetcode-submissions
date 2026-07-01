class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i : [] for i in range(n) }
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        visited = set()
        components = 0

        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for neighbor in adjList[curr]:
                dfs(neighbor)

        for i in adjList:
            if i not in visited:
                components += 1
                dfs(i)

        return components
                    