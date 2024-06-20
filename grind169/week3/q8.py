class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*(n+1)
        pre[0] = nums[0]
        post = [1]*(n+1)
        post[n-1] = nums[n-1]
        
        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            post[i] = post[i+1]*nums[i]
        
        ans = [1]*n
        ans[0] = post[1]
        ans[n-1] = pre[n-2]
        for i in range(1,n-1):
            ans[i] = pre[i-1]*post[i+1]        

        return ans
    
    # space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        # first use ans as pre
        ans[0] = nums[0]
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i]
        # use ans as result
        ans[n-1] = ans[n-2]
        postMulti = 1
        for i in range(n-2,0,-1):
            postMulti *= nums[i+1]
            ans[i] = ans[i-1]*postMulti
        ans[0] = postMulti*nums[1]
        return ans