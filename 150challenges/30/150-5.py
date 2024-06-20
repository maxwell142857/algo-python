class Solution:
    # solution1: hashmap
    def majorityElement(self, nums: List[int]) -> int:
        check = {}
        n = len(nums)
        for element in nums:
            updateValue = check.get(element,0)+1
            if updateValue > n//2:
                return element
            check[element] = updateValue
        return 0    
    # solution2: Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        element = -1
        cnt = 0
        for item in nums:
            if cnt == 0:
                element = item
                cnt += 1
            else:
                if element == item:
                    cnt += 1
                else:
                    cnt -= 1
        return element    