class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def check(i,j):
            s1 = words[i]
            s2 = words[j]
            if s1 > s2:
                return False
            l = len(s1)
            return s2[:l]==s1 and s2[-l:]==s1
        
        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i+1,n):
                if check(i,j):
                    cnt += 1
        return cnt