from typing import List


class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.neighbors = {}
        self.word = ""



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build prefix tree for words
        root = Node(0)
        for word in words:
            pointer = root
            for letter in word:
                if letter in pointer.neighbors:
                    pointer = pointer.neighbors[letter]
                else:
                    newNode = Node(letter)
                    pointer.neighbors[letter] = newNode
                    pointer = newNode
            pointer.word = word


        # run DFS on prefix tree and run DFS on board
        rowCnt = len(board)
        colCnt = len(board[0]) 
        visited = set()
        ans = set()

        def DFS(pointer,r,c):
            nonlocal ans

            if pointer.word != "":
                ans.add(pointer.word)

            # backtracking
            biasR = [1,-1,0,0]
            biasC = [0,0,1,-1]

            for biasIndex in range(4):
                rr = r+biasR[biasIndex]
                cc = c+biasC[biasIndex]
                if rr < rowCnt and rr >= 0 and cc < colCnt and cc >= 0 and (rr,cc) not in visited \
                and board[rr][cc] in pointer.neighbors:
                    nextPointer = pointer.neighbors[board[rr][cc]]
                    visited.add((rr,cc))
                    DFS(nextPointer,rr,cc)
                    visited.remove((rr,cc))
        

        for i in range(rowCnt):
            for j in range(colCnt):
                if board[i][j] in root.neighbors:
                    visited.add((i,j))
                    DFS(root.neighbors[board[i][j]],i,j)
                    visited.remove((i,j))
            
        return list(ans)

        
        
    
# s = Solution()

# print(s.findWords([["a","b"],["c","d"]],["abdc","ac"]))