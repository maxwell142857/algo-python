class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        leftD = [10**4+1]*n
        if s[0] == c:
            leftD[0] = 0
        for i in range(1,n):
            if s[i] == c:
                leftD[i] = 0
            else:
                leftD[i] = leftD[i-1]+1
        rightD = [10**4+1]*n
        if s[n-1] == c:
            rightD[n-1] = 0
        for i in range(n-2,-1,-1):
            if s[i] == c:
                rightD[i] = 0
            else:
                rightD[i] = rightD[i+1]+1
        ans = [0]*n
        for i in range(n):
            ans[i] = min(leftD[i],rightD[i])
        return ans
        
