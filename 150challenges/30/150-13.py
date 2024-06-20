class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preMulti = [1]*n
        for i in range(1,n):
            preMulti[i] = preMulti[i-1]*nums[i-1]
        postMulti = 1
        ans = [0]*n
        ans[n-1] = preMulti[n-1]
        for i in range(n-2,-1,-1):
            postMulti *= nums[i+1]
            ans[i] = preMulti[i]*postMulti
        return ans