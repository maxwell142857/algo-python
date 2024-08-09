class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        nums = []
        for c in columnTitle:
            nums.append(ord(c)-ord('A')+1)
        power = len(nums)-1
        ans = 0
        for val in nums:
            ans += pow(26,power)*val
            power -= 1
        return ans