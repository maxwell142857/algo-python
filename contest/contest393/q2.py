class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(num):
            if num == 1:
                return False
            for i in range(2,11):
                if i>=num:
                    return True
                if num%i==0:
                    return False
            return True
        
        indexs = []
        for i in range(len(nums)):
            if isPrime(nums[i]):
                indexs.append(i)

        if len(indexs) == 1:
            return 0
        else:
            return indexs[-1]-indexs[0]