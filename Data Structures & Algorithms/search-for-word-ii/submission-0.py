class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie construction
        root = Node()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node()
                curr = curr.children[char]
            curr.isEnd = True

        # Backtracking
        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEnd:
                res.add(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)

            

