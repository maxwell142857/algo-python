class Solution:
    def checkValidString(self, s: str) -> bool:
        def check(s):
            starCnt = 0
            leftCnt = 0
            for c in s:
                if c =='(':
                    leftCnt += 1
                elif c == ')':
                    leftCnt -= 1
                    if leftCnt < 0:
                        if starCnt !=0:
                            starCnt -= 1
                            leftCnt = 0
                        else:
                            return False
                else:
                    starCnt += 1
            return leftCnt <= starCnt
        newS = ''
        for c in s:
            if c == '(':
                newS += ')'
            elif c ==')':
                newS += '('
            else:
                newS += c
        return check(s) and check(newS[::-1])
    
    def checkValidString(self, s: str) -> bool:
        leftCnt = 0
        for c in s:
            if c == '(' or c == '*':
                leftCnt += 1
            else:
                leftCnt -= 1 
                if leftCnt < 0:
                    return False
        
        rightCnt = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            c = s[i]
            if c == ')' or c == '*':
                rightCnt += 1
            else:
                rightCnt -= 1 
                if rightCnt < 0:
                    return False
        return True