class Solution:
    # O(n^2) DP TLE
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable = [False]*n
        reachable[0] = True
        for i in range(1,n):
            for j in range(i):
                if reachable[j] and j+nums[j]>=i:
                    reachable[i] = True
                    if reachable[n-1]:
                        return True
        return reachable[n-1]
    
    # O(n) greedy
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxDis= 0
        for i in range(n):
            if i <= maxDis:
                maxDis = max(maxDis,i+nums[i])
                if maxDis >= n-1:
                    return True
            else:
                return False
        return False
