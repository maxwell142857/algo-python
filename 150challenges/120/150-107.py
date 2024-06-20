class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        rCnt = len(board)
        cCnt = len(board[0])

        # preprocessing
        frequency = {}
        for i in range(rCnt):
            for j in range(cCnt):
                letter = board[i][j]
                frequency[letter] = frequency.get(letter,0)+1
        for letter in word:
            if letter not in frequency:
                return False
            
        if frequency[word[0]] > frequency[word[-1]]:
            word = word[::-1]


        # index is the target index in word, (r,c) is the current position try to visit
        def backtracking(index,r,c):
            nonlocal ans
            if index == len(word):
                return True 
            
            if r==rCnt or r<0 or c==cCnt or c<0 or word[index] != board[r][c]:
                return False
            
            rBias = [0,0,1,-1]
            cBias = [1,-1,0,0]

            letter = board[r][c]
            board[r][c] = '#'
            result = False
            for i in range(4):
                rr = r+rBias[i]
                cc = c+cBias[i]
                result = result or backtracking(index+1,rr,cc)
            board[r][c] = letter
            return result
        
        for i in range(rCnt):
            for j in range(cCnt):
                if backtracking(0,i,j):
                    return True
        return False