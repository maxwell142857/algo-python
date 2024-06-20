class Solution:
    # O(n*lgn)
    def countBits(self, n: int) -> List[int]:
        def count(number):
            result = 0
            while number:
                result += number%2
                number //= 2
            return result
        
        ans = []
        for i in range(n+1):
            ans.append(count(i))
        return ans
    # O(n)
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        path = 2
        pathCnt = 0
        ans = [0]*(n+1)
        ans[0] = 0
        ans[1] = 1
        for i in range(2,n+1):
            if pathCnt == path:
                pathCnt = 0
                path *= 2
            ans[i] =  ans[i-path]+1
            pathCnt += 1
        return ans