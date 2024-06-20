class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(pattern)

        def checkPattern(target):
            for i in range(n):
                if pattern[i]==0 and target[i]==target[i+1]:
                    continue
                elif pattern[i]==1 and target[i]<target[i+1]:
                    continue
                elif pattern[i]==-1 and target[i]>target[i+1]:
                    continue
                else:
                    return False
            return True
        
        length = len(nums)
        ans = 0
        for i in range(length):
            if i+n+1>length:
                break
            if checkPattern(nums[i:i+n+1]):
                ans += 1
        
        return ans