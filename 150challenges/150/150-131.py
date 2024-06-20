class Solution:

    # convert to string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        def number2string(number):
            result = []
            while number:
                result.append(number%10)
                number //= 10
            result.reverse()
            return result

        s = number2string(x)
        n = len(s)
        start = 0
        end = n-1
        while start <= end and s[start] == s[end] :
            start += 1
            end -= 1
        return start > end
            
    # not convert to string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        number = x
        cnt = 0
        while number:
            number //= 10
            cnt += 1
        if cnt%2 == 0:
            half = cnt//2
            left = x // (10**half)
            right = x% (10**half)
        else:
            half = cnt//2
            left = x // (10**(half+1))
            right = x % (10**half)
        
        base = 10**(half-1)
        reverseLeft = 0
        while left:
            reverseLeft += (left%10)*base
            left //= 10
            base //= 10
        return reverseLeft == right