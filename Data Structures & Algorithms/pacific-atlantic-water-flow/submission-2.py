class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        width, height = len(heights[0]), len(heights)
        result = []

        def bfs(x, y, onPacific):
            q = collections.deque()
            q.append((x,y))

            while q:
                x, y = q.popleft()

                if onPacific:
                    if (x,y) in pacific:
                        continue
                    pacific.add((x, y))
                else:
                    if (x,y) in atlantic:
                        continue
                    atlantic.add((x, y))
                
                # Left 
                if y-1 >= 0 and heights[x][y-1] >= heights[x][y]:
                    q.append((x, y-1))

                # Right
                if y+1 < width and heights[x][y+1] >= heights[x][y]:
                    q.append((x, y+1))

                # Top
                if x+1 < height and heights[x+1][y] >= heights[x][y]:
                    q.append((x+1, y))

                # Bottom
                if x-1 >= 0 and heights[x-1][y] >= heights[x][y]:
                    q.append((x-1, y))

        # BFS on Pacific
        # Top
        for i in range(width):
            bfs(0, i, True)
        
        # Left
        for j in range(height):
            bfs(j, 0, True)

        # BFS on Atlantic
        # Bottom
        for i in range(width):
            bfs(height-1, i, False)
        
        # Right
        for j in range(height):
            bfs(j, width-1, False)

        # Return overlapping coordinates
        for node in pacific:
            if node in atlantic:
                result.append([node[0], node[1]])
        
        return result
