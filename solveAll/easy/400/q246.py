class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        def getReverse(c):
            if c in '018':
                return c
            if c == '6':
                return '9'
            if c == '9':
                return '6'
        
        n = len(num)
        p1,p2 = 0,n-1
        legal = '01869'
        while p1 <= p2:
            if num[p1] in legal and num[p2] in legal and num[p1] == getReverse(num[p2]):
                p1 += 1
                p2 -= 1
            else:
                return False
        return True