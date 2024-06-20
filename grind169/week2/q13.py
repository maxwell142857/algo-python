class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverseNubmer(number):
            result = []
            while number:
                result.append(number%10)
                number //= 10
            l = len(result)
            ans = 0
            for i in range(l):
                ans += result[i]*10**(l-i-1)
            return ans
        
        if x < 0:
            return False
        else:
            return x == reverseNubmer(x)
