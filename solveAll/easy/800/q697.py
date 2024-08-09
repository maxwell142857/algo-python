from collections import Counter,defaultdict
class Solution:
    # sliding windows
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = Counter(nums)
        degree = max(counter.values())
        left = 0
        val2cnt = defaultdict(int)
        ans = len(nums)
        for right in range(len(nums)):
            val2cnt[nums[right]] += 1
            if val2cnt[nums[right]] == degree:
                while val2cnt[nums[right]] == degree:
                    val2cnt[nums[left]] -= 1
                    left += 1
                ans = min(ans,right-left+2)
        return ans
    
    # based on question
    def findShortestSubArray(self, nums: List[int]) -> int:
        val2cnt = defaultdict(int)
        firstIndex = {}
        lastIndex = {}
        n = len(nums)
        for i in range(n):
            val  = nums[i]
            val2cnt[val] += 1
            if val not in firstIndex:
                firstIndex[val] = i
            lastIndex[val] = i

        degree = max(val2cnt.values())
        ans = len(nums)
        for k in val2cnt.keys():
            if val2cnt[k] == degree:
                ans = min(ans,lastIndex[k]-firstIndex[k]+1)
        return ans