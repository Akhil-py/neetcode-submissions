class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(word, node):
            if word == "": 
                return node.isEnd

            if word[0] in node.children:
                return dfs(word[1::], node.children[word[0]])
            
            if word[0] == '.':
                found = False
                for i in node.children:
                    found = found or dfs(word[1::], node.children[i])
                return found
            else:
                return False

        return dfs(word, self.root)