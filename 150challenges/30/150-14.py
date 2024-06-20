
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas *= 2
        cost *= 2
        n = len(gas)
        remainGas = 0
        start = 0
        stationCnt = 0
        for i in range(n):
            remainGas += gas[i]-cost[i]
            if remainGas >= 0:
                stationCnt += 1
                if stationCnt == n//2:
                    return start
            else:
                remainGas = 0
                start = i+1
                stationCnt = 0
        return -1
    
s = Solution()
s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
