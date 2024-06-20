class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number = 0
        cnt = 0
        for num in nums:
            if cnt == 0:
                number = num
                cnt = 1
            else:
                if num == number:
                    cnt += 1
                else:
                    cnt -= 1
        return number