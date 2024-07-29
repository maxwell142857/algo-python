class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(val):
            if val ==0:
                return mapping[0]
            
            result = []
            while val:
                result.append(str(mapping[val%10]))
                val //= 10
            result = result[::-1]
            return int(''.join(result))
        
        array = []
        n = len(nums)
        for i in range(n):
            array.append((convert(nums[i]),i,nums[i]))
        array.sort(key = lambda x:(x[0],x[1]))
        ans = [val[2] for val in array]
        return ans

