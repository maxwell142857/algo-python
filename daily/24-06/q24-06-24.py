from collections import deque
class Solution:
    # greedy+simulaition, the pointer goes back
    # O(n*k), TLE
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = 0
        cnt = 0
        while True:
            while p<n and nums[p] == 1:
                p += 1 
            if p == n:
                return cnt
            if n-p < k:
                return -1
            else:
                # flip
                cnt += 1
                for i in range(p,p+k):
                    nums[i] = (nums[i]+1)%2
                    if p == i and nums[i] == 1:
                        p += 1
    # greedy+simulaition, the pointer does not go back
    # O(n)
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        isFlipped = [False]*n
        currentFlipCnt = 0
        cnt = 0
        for i in range(n):
            if i>=k and isFlipped[i-k]:
                currentFlipCnt -= 1
            if (nums[i]+currentFlipCnt)%2 == 0:
                # we need flip
                if i > n-k:
                    return -1
                isFlipped[i] = True
                currentFlipCnt += 1
                cnt += 1
        return cnt
            
            
            