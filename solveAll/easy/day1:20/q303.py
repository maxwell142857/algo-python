class NumArray:

    def __init__(self, nums: List[int]):
        pre = 0
        self.preSum = [0]
        for val in nums:
            self.preSum.append(val+pre)
            pre += val

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1]-self.preSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)