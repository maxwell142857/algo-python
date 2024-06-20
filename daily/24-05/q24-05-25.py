class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        path = []
        ans = []
        words = set(wordDict)
        def backtracking(index):
            if index==n:
                ans.append(' '.join(path[:]))
                return
            
            for i in range(index+1,n+1):
                if s[index:i] in words:
                    path.append(s[index:i])
                    backtracking(i)
                    path.pop()
        
        backtracking(0)
        return ans

