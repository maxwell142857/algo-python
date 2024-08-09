class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def checkDividing(val):
            digits = str(val)
            for digit in digits:
                d = int(digit)
                if d == 0:
                    return False
                if val%d != 0:
                    return False
            return True
        
        ans = []
        for val in range(left,right+1):
            if checkDividing(val):
                ans.append(val)
        return ans
            
