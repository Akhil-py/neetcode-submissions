class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Verify Rows
        for row in board:
            seen = set()
            for x in row:
                if x != "." and x in seen:
                    return False
                seen.add(x)

        # Verify Columns
        for y in range(len(board)):
            seen = set()
            for x in range(len(board[0])):
                if board[x][y] != "." and board[x][y] in seen:
                    return False
                seen.add(board[x][y])

        # Verify 3x3 boxes
        for box_y in range(0, 9, 3):
            for box_x in range(0, 9, 3):
                seen = set()
                for y in range(box_y, box_y + 3):
                    for x in range(box_x, box_x + 3):
                        if board[y][x] != "." and board[y][x] in seen:
                            return False
                        seen.add(board[y][x])

        # If all requirements pass        
        return True