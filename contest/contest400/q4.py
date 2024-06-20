class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n  =len(nums)
        bits = [[0]*32 for _ in range(n)]
        for i in range(n):
            val = nums[i]
            p = 0
            while val > 0:
                bits[i][p] = val%2
                p += 1
                val //= 2
        
        # preSum
        for i in range(1,n):
            for j in range(32):
                bits[i][j] += bits[i-1][j]

        # sliding windows
        def state2val(start,end):
            arr2 = bits[end]
            if start == 0:
                arr1 = [0]*32
            else:
                arr1 = bits[start-1]
            
            val = 0
            for i in range(32):
                if arr2[i]-arr1[i] == end-start+1:
                    val += 2**i
            return val
        
        left = 0
        state = [0]*32
        ans = float('inf')
        for right in range(n):
            
            val = state2val(left,right)
            ans = min(ans,abs(val-k))
            while left<right and val < k:
                left += 1
                val = state2val(left,right)
                ans = min(ans,abs(val-k))
                
        return ans
            
            