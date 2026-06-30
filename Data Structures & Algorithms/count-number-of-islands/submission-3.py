class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    visited.add((i,j))
                if (i,j) in visited:
                    continue

                # DFS
                islands += 1
                stack = []
                stack.append((i,j))
                while stack:
                    x,y = stack.pop()
                    
                    if grid[x][y] == "1" and (x,y) not in visited:
                        # Add neighbors to stack
                        # Top
                        if x-1 >= 0:
                            stack.append((x-1,y))
                        # Left
                        if y-1 >= 0:
                            stack.append((x,y-1))
                        # Bottom
                        if x+1 < len(grid):
                            stack.append((x+1,y))
                        # Right
                        if y+1 < len(grid[0]):
                            stack.append((x, y+1))
                    visited.add((x,y))
                        
                    
        return islands



