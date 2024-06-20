class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        mask = 0
        for i in range(29,-1,-1):
            mask = mask | (1<<i)
            tmp = mask
            cnt = 0
            for num in nums:
                tmp = tmp & num
                if (tmp | ans) != ans:
                    cnt += 1
                else:
                    tmp = mask
            if cnt > k:
                ans = ans | (1<<i)
        return ans
        
        
#111111111111111000000000000000
#000000000000001000000000000000