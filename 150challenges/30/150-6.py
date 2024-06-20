class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        copy = nums[:]
        for index, item in enumerate(copy):
            nums[(index+k)%n] = item
            