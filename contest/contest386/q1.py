from typing import List
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        num2cnt = {}
        for num in nums:
            num2cnt[num] = num2cnt.get(num,0)+1
            if num2cnt[num] == 3:
                return False
            
        return True
s = Solution()
s.isPossibleToSplit([1,2,3])
print("le")