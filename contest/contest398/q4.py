import math
class Solution:
    def waysToReachStair(self, k: int) -> int:
        
        # use total t operations,x op1 and y op2
        def checkT(t):
            # x+y = t, y-x<=1
            # 2^x-1-y = k-1  --> 2^x = y+k
            # 2^x = -x+t+k
            result = -1
            for x in range(t+1):
                if pow(2,x) == -x+t+k:
                    result = x
                    break
            if result != -1:
                x = result
                y = t-x
                # check y-x<=1
                if y-x<=1:
                    return math.comb(x+1,y)
                else:
                    return 0
            else:
                return 0
            
        ans = 0
        # 2^(64//2) > 10^9
        # I choose 100 as 100 > 64
        # this range can be smaller and more precise
        for i in range(100):
            ans += checkT(i)
        return ans