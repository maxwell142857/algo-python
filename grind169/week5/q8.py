class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        delta = [0]*n
        for i in range(n):
            delta[i] = gas[i]-cost[i]
        start = 0
        
        while start<n:
            storage = 0
            offset = 0
            while offset < n:
                storage += delta[(start+offset)%n]
                if storage < 0:
                    break
                offset += 1
            if storage >= 0:
                return start
            else:
                start += offset+1
        return -1