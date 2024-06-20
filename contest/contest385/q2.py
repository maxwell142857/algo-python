class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def getLength(num):
            cnt = 0
            while num > 0:
                num //= 10
                cnt += 1
            return cnt
        
        prefixSet = set()
        for number in arr1:
            while number > 0:
                prefixSet.add(number)
                number //= 10
        
        ans = 0

        for number in arr2:
            while number > 0:
                if number in prefixSet:
                    ans = max(ans,getLength(number))
                    break
                number //= 10
        return ans