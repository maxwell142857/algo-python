class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2index = {}
        for index,item in enumerate(nums):
            if target-item in value2index:
                return [index,value2index[target-item]]
            value2index[item] = index