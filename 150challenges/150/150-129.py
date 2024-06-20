class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0]*32
        for number in nums:
            number += 2**31
            index = 0
            while number:
                if number%2:
                    bits[index] = (bits[index]+1)%3
                number //= 2
                index += 1
        base = 1
        ans = 0
        for bit in bits:
            if bit:
                ans += base
            base *= 2
        return ans -2**31
