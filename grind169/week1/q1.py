class Solution:
    # sort + Bsearch, O(n*lgn)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        numsWithID = []
        for i in range(n):
            numsWithID.append((nums[i],i))
        numsWithID.sort()
        for i in range(n):
            left = i+1
            right = n-1
            while left <= right:
                mid = (left+right)//2
                if numsWithID[mid][0]+numsWithID[i][0]==target:
                    return[numsWithID[i][1],numsWithID[mid][1]]
                elif numsWithID[mid][0]+numsWithID[i][0]>target:
                    right = mid-1
                else:
                    left = mid+1
        return []
    
    # hashmap, O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        val2id = {}
        for i in range(n):
            if target-nums[i] in val2id:
                return [val2id[target-nums[i]],i]
            val2id[nums[i]] = i