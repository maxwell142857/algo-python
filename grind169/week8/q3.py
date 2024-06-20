class Number:
    def __init__(self,val) -> None:
        self.val = str(val)
    
    def __lt__(self,other):
        return self.val+other.val > other.val+self.val

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers = [Number(num) for num in nums]
        numbers.sort()
        result =  ''.join(s.val for s in numbers)
        if result[0] == '0':
            return '0'
        else:
            return result