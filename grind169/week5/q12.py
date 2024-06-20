class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        preMul = 1
        leastPre = 0
        ans = nums[0]
        for i in range(n):
            if nums[i] == 0:
                preMul = 1
                leastPre = 0
                ans = max(ans,0)
            else:
                preMul *= nums[i]
                if preMul>0:
                    ans = max(ans,preMul)
                else:
                    if leastPre == 0:
                        leastPre = preMul
                    else:
                        ans = max(ans,preMul//leastPre)
        return ans

