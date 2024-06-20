class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.neighbors = []

class WordDictionary:

    def __init__(self):
        self.root = Node(0)

    def addWord(self, word: str) -> None:
        current = self.root
        for index in range(0,len(word)):
            insertChar = word[index]
            find = False 

            for son in current.neighbors:
                if son.val == insertChar:
                    # find the char
                    find = True
                    current = son
                    break
            
            if not find:
                newNode = Node(insertChar)
                current.neighbors.append(newNode)
                current = newNode
        current.neighbors.append(Node(0))

    def search(self, word: str) -> bool:
        find = False

        def DFS(currentNode,word,targetIndex):
            nonlocal find

            if targetIndex == len(word):
                for son in currentNode.neighbors:
                    if son.val == 0:
                        find = True
                return

            targetChar = word[targetIndex]
            if targetChar == '.':
                for son in currentNode.neighbors:
                    DFS(son,word,targetIndex+1)
            else:
                for son in currentNode.neighbors:
                    if son.val == targetChar:
                        DFS(son,word,targetIndex+1)

        DFS(self.root,word,0)
        return find