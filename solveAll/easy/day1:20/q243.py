class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = []
        index2 = []
        for i,w in enumerate(wordsDict):
            if w==word1:
                index1.append(i)
            if w==word2:
                index2.append(i)
        p1,p2 = 0,0
        ans = abs(index1[0]-index2[0])
        while p1 < len(index1) and p2 < len(index2):
            ans = min(ans,abs(index1[p1]-index2[p2]))
            if index1[p1] > index2[p2]:
                p2 += 1
            else:
                p1 += 1
        return ans