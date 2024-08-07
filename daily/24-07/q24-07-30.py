class Solution:
    # preSum, O(n)
    def minimumDeletions(self, s: str) -> int:
        totalA,totalB = 0,0
        n = len(s)
        for c in s:
            if c == 'a':
                totalA += 1
            else:
                totalB += 1
        ans = totalA
        curA,curB = 0,0
        for i in range(n):
            if s[i] == 'a':
                curA += 1
            else:
                curB += 1
            # aaaa s[i] bbbbb
            cost1 = curB
            cost2 = totalA-curA
            ans = min(ans,cost1+cost2)
        return ans

    # dp, O(n)
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        cost = [0]*n
        cntB = 0
        if s[0] == 'b':
            cntB += 1
        for i in range(1,n):
            if s[i] == 'a':
                # delete this one, or delete all b before it
                cost[i] = min(cost[i-1]+1,cntB)
            else:
                cost[i] = cost[i-1]
                cntB += 1
        return cost[n-1]  

    # dp O(n)
    # space optimized
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        cost = 0
        cntB = 0
        if s[0] == 'b':
            cntB += 1
        for i in range(1,n):
            if s[i] == 'a':
                # delete this one, or delete all b before it
                cost = min(cost+1,cntB)
            else:
                cntB += 1
        return cost  



