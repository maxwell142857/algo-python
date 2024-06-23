from collections import defaultdict
class Solution:
    # brute force
    # O(n^2*l)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        ans = []
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                combination = words[i]+words[j]
                if combination == combination[::-1]:
                    ans.append([i,j])
        return ans


    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        s2index = defaultdict(list)
        for i,w in enumerate(words):
            s2index[w].append(i)

        for i in range(n):
            word = words[i]
            
        
