class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cnt = len(words)

        def get(i,j):
            if i<cnt and len(words[i])>j:
                return words[i][j]
            else:
                return '!'
        
        
        n = cnt
        for i in range(cnt):
            n =  max(n,len(words[i]))
        for i in range(n):
            for j in range(i+1,n):
                if get(i,j)!= get(j,i):
                    return False
        return True