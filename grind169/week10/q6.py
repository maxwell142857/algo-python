class Solution:
    # TLE
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     rowCnt = len(board)
    #     colCnt = len(board[0])

        
    #     def find(r,c,word,index):
    #         nonlocal get
    #         if get:
    #             return
            
    #         if index == len(word)-1:
    #             get = True
    #             return
                
                
    #         bias = [[0,1],[1,0],[0,-1],[-1,0]]
    #         for i in range(4):
    #             rr = r+bias[i][0]
    #             cc = c+bias[i][1]
    #             if 0<=rr<rowCnt and 0<=cc<colCnt and board[rr][cc] == word[index+1]:
    #                 save = board[rr][cc]
    #                 board[rr][cc] = '*'
    #                 find(rr,cc,word,index+1)
    #                 board[rr][cc] = save
        
    #     ans = []
    #     for w in words:
    #         get = False
    #         for i in range(rowCnt):
    #             for j in range(colCnt):
    #                 if not get and board[i][j] == w[0]:
    #                     save = board[i][j]
    #                     board[i][j] = '*'
    #                     find(i,j,w,0)
    #                     board[i][j] = save
    #         if get:
    #             ans.append(w)
    #     return ans
            

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            p = root
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['*'] = {}

        rowCnt = len(board)
        colCnt = len(board[0])

        ans = set()
        def DFS(r,c,p,path):

            char = board[r][c]
            if char in p:

                board[r][c] = '!'
                path += char
                if '*' in p[char]:
                    ans.add(path)
                    p[char].pop('*')

                bias = [[0,1],[1,0],[0,-1],[-1,0]]
                for i in range(4):
                    rr = r+bias[i][0]
                    cc = c+bias[i][1]
                    if 0<=rr<rowCnt and 0<=cc<colCnt:
                        DFS(rr,cc,p[char],path)
                
                board[r][c] = char
                
                if not p[char]:
                    p.pop(char)


        for i in range(rowCnt):
            for j in range(colCnt):
                DFS(i,j,root,'')
        return list(ans)
