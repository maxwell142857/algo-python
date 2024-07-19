class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        mySum = sum(nums[:k])
        ans = mySum
        for right in range(k,n):
            mySum += nums[right]
            mySum -= nums[right-k]
            ans = max(ans,mySum)
        return ans/k
