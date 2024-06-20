class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.neighbors = []


class Trie:

    def __init__(self):
        self.root = Node(0)
        
    def insert(self, word: str) -> None:
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
        current = self.root
        for index in range(0,len(word)):
            searchChar = word[index]
            find = False 
            for son in current.neighbors:
                if son.val == searchChar:
                    # find the char
                    find = True
                    current = son
                    break
            if not find:
                return False
        # check whether there is an end node
        for son in current.neighbors:
            if son.val == 0:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for index in range(0,len(prefix)):
            searchChar = prefix[index]
            find = False 
            for son in current.neighbors:
                if son.val == searchChar:
                    # find the char
                    find = True
                    current = son
                    break
            if not find:
                return False
        return True

