class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        copy = score[:]
        copy.sort(reverse = True)
        val2ans = {}
        val2ans[copy[0]] = "Gold Medal"
        if n>=2:
            val2ans[copy[1]] = "Silver Medal"
        if n>=3:
            val2ans[copy[2]] = "Bronze Medal"
        for i in range(3,n):
            val2ans[copy[i]] = str(i+1)
        ans = []
        for s in score:
            ans.append(val2ans[s])
        return ans