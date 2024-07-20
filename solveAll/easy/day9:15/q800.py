class Solution:
    def similarRGB(self, color: str) -> str:
        
        def getS(val):
            diff = 16**2 # 100
            ans = 0
            for i in range(16):
                cur = i*17
                if abs(cur-val) < diff:
                    diff = abs(cur-val)
                    ans = cur
            return hex(ans)[-1]*2
        
        ans = '#'
        for i in range(1,7,2):
            val = int(color[i:i+2],16)
            ans += getS(val)
        return ans


