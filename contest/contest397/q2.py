class Solution:
    # brute force,O(n^2), TLE
    # def maximumEnergy(self, energy: List[int], k: int) -> int:
    #     n = len(energy)
    #     ans = float('-inf')
    #     for start in range(n):
    #         tmp = 0
    #         cur = start
    #         while cur < n:
    #             tmp += energy[cur]
    #             cur += k
    #         ans = max(ans,tmp)

    #     return ans
    
    # preSum,O(n)
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float('-inf')
        for start in range(k):
            preSum = 0
            cur = start
            while cur < n:
                if preSum<0:
                    preSum = energy[cur]
                else:
                    preSum += energy[cur]
                cur += k
            ans = max(ans,preSum)
        return ans