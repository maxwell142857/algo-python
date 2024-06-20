class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0]*n
        pre[0] = 1
        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]
        print(pre)
        ans = [0]*n
        suffix = 1
        for i in range(n-1,-1,-1):
            ans[i] = pre[i]*suffix
            suffix *= nums[i]
        return ans