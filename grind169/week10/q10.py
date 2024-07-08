from collections import defaultdict
class Solution:
    # brute force
    # TLE
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

    # O(n*l^2)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        s2index = defaultdict(list)
        for i,w in enumerate(words):
            s2index[w].append(i)

        ans = []
        for i in range(n):
            word = words[i]
            l = len(word)
            # a+a'
            for c in s2index[word[::-1]]:
                if c!=i:
                    ans.append([c,i])
            # a+Ba, where B is palindrome, this word is Ba
            for j in range(1,l+1):
                prefix = word[:j]
                if prefix == prefix[::-1]:
                    remain = word[j:]
                    for c in s2index[remain[::-1]]:
                        if c != i:
                            ans.append([c,i])
            # bA+b, where A is palindrome, this word is bA
            for j in range(l-1,-1,-1):
                suffix = word[j:]
                if suffix == suffix[::-1]:
                    remain = word[:j]
                    for c in s2index[remain[::-1]]:
                        if c != i:
                            ans.append([i,c])
        return ans
