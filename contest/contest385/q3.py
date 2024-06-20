class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        direction = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        rowCnt = len(mat)
        colCnt = len(mat[0])
        number2frequency = {}

        def DFS(r,c,val,direct):
            val  = val*10+mat[r][c]
            if val > 10:
                number2frequency[val] = number2frequency.get(val,0)+1
            nextR = r+direct[0]
            nextC = c+direct[1]
            if 0<=nextR<rowCnt and 0<=nextC<colCnt:
                DFS(nextR,nextC,val,direct)

        def checkPrime(number):
            mod = 2
            while mod*mod <= number:
                if number%mod==0:
                    return False
                mod += 1
            return True
        
        for i in range(rowCnt):
            for j in range(colCnt):
                for index in range(len(direction)):
                    DFS(i,j,0,direction[index])
        
        ansKey = -1
        ansVal = 0
        for key,val in number2frequency.items():
            if checkPrime(key):
                if val > ansVal or (val==ansVal and key > ansKey):
                    ansKey = key
                    ansVal = val

        return ansKey
        