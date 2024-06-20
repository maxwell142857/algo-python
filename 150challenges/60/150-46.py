class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value2index = {}
        for index in range(len(nums)):
            val = nums[index]
            if val in value2index and index- value2index[val] <= k:
                return True
            value2index[val] = index
        return False