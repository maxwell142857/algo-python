class Solution:
    # recursive with memo
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        memo = {} # word:bool
        def check(start,end):
            word = s[start:end]
            if word in memo:
                return memo[word]
            
            n = len(word)
            if word in dictionary:
                return True
            find = False
            for i in range(1,n):
                if check(start,start+i) and check(start+i,end):
                    find = True
                    break
            memo[word] = find
            return find
        
        return check(0,len(s))
    # dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        n = len(s)
        for i in range(1,n+1):
            if s[:i] in dictionary:
                continue
            # check are s[:j] and s[j:i] in dictionary by iterate j
            for j in range(i):
                if s[:j] in dictionary and s[j:i] in dictionary:
                    dictionary.add(s[:i])
                    break
        return s in dictionary
    
    # dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        n = len(s)
        dp = [False]*(n+1) # dp[i] mean s[:i] can be make up
        for i in range(1,n+1):
            if s[:i] in dictionary:
                dp[i] = True
                continue
            # check are s[:j] and s[j:i] in dictionary by iterate j
            for word in wordDict:
                length = len(word)
                if s[i-length:i] == word and dp[i-length]:
                    dp[i] = True
                    break
        return dp[n]