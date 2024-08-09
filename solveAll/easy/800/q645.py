class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = set()
        ans = []
        for num in nums:
            if num in check:
                ans.append(num)
                break
            else:
                check.add(num)
        check = set(nums)
        for i in range(1,len(nums)+1):
            if i not in check:
                ans.append(i)
        return ans