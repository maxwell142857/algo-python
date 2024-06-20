class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = 0
        for num in nums:
            if num%2 == 0:
                cnt += 1
                if cnt == 2:
                    return True
        return False