class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mySet = set(wordDict)
        n = len(s)
        memo = [-1]*(n+1) # -1 for unknown,1 for true,0 for false
        def solve(endIndex):
            if endIndex == 0:
                return True
            if memo[endIndex] != -1:
                return memo[endIndex]
            
            flag = False
            for word in wordDict:
                length = len(word)
                if s[endIndex-length:endIndex] in mySet:
                    flag  = solve(endIndex-length)
                    if flag:
                        break
            
            if flag:
                memo[endIndex] = 1
            else:
                memo[endIndex] = 0
            return flag
        
        return solve(n)

