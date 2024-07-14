class Solution:
    def convertToBase7(self, num: int) -> str:
        def convert(val):
            result = []
            while val:
                result.append(str(val%7))
                val //= 7
            result = result[::-1]
            return ''.join(result)
        
        if num>0:
            return convert(num)
        elif num == 0:
            return '0'
        else:
            return '-'+convert(-num)