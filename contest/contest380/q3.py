class Solution:
    # brute force, TLE
    def findMaximumNumber(self, k: int, x: int) -> int:
        def calculatePrice(number):
            price = 0
            number = number<<1
            while number:
                number = number>>x
                if number & 1:
                    price += 1
            return price

        total = 0
        index = 1
        while True:
            total += calculatePrice(index)
            if total > k:
                return index-1
            
            index += 1
    
    # 
    def findMaximumNumber(self, k: int, x: int) -> int:
        def check(number):
            totalPrice = 0
            digitCnt = 0
            numberCopy = number
            while numberCopy:
                numberCopy >>= 1
                digitCnt += 1
            for digitIndex in range(1,digitCnt+1):
                if digitIndex%x == 0:
                    elementCnt = number - (2**(digitIndex-1)-1)
                    totalPrice += elementCnt//(2**digitIndex)*(2**digitIndex)/2
                    elementCnt = elementCnt%(2**digitIndex)
                    totalPrice += min(elementCnt,2**(digitIndex-1))
            
            return totalPrice <= k
        
        left = 1
        right = 2**64
        while left < right:
            mid = (left+right+1)//2
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left
    
def check(number):
            totalPrice = 0
            digitCnt = 0
            numberCopy = number
            while numberCopy:
                numberCopy >>= 1
                digitCnt += 1
            for digitIndex in range(1,digitCnt+1):
                    elementCnt = number - (2**(digitIndex-1)-1)
                    totalPrice += elementCnt//(2**digitIndex)*2
                    elementCnt = elementCnt%(2**digitIndex)
                    totalPrice += min(elementCnt,2**(digitIndex-1))
            
            return totalPrice
check(6)