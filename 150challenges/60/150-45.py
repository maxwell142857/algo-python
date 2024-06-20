class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        number = n
        while number not in visited:
            if number == 1:
                return True
            else:
                visited.add(number)
                number = digitSum(number)

def digitSum(n):
    ans = 0
    while n > 0:
        ans += (n%10)**2
        n //= 10
    return ans