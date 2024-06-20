# for each space with length k
# f(k) = f(k-1)*2 and f(1) = 1 thus f(k) = 2^(k-1)
# f(k) / A(k,k) is the possibility of random generation
# total space is t, there are t^t random generation
# need to compute 

from typing import List


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        mod = 10**9+7
        space = []
        for index in range(1,len(sick)):
            peopleCnt = sick[index]-sick[index-1]-1
            if peopleCnt != 0:
                space.append(sick[index]-sick[index-1]-1)
        if sick[0]!= 0:
            space.append(sick[0])
        if sick[len(sick)-1] != n-1:
            space.append(n-1-sick[len(sick)-1])
        maxSapce = max(space)
        spaceCnt = n - len(sick)
        valid = [1]
        for i in range(1,maxSapce+1):
            valid.append(valid[i-1]*2)
        all = [1]
        for i in range(1,maxSapce+1):
            all.append(all[i-1]*(i+1))
        ans = 1
        for i in range(2,spaceCnt+1):
            ans *= i
        for item in space:
            ans =  ans * valid[item-1]//all[item-1]
        return ans%mod
s = Solution()
s.numberOfSequence(5,[0,4])