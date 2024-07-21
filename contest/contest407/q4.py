class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        diff = []
        for i in range(n):
            diff.append(nums[i]-target[i])
        
        def cost(l,r):
            if l<0 or r>n or l>=r:
                return 0
            if diff[l] < 0:
                # change all value to positive
                for i in range(l,r):
                    diff[i] = -diff[i]
            if l+1 == r:
                return diff[l]
            
            minVal = min(diff[l:r])
            cnt = 0
            preZeroIndex = l-1
            for i in range(l,r):
                diff[i] -= minVal
                if diff[i] == 0:
                    cnt += cost(preZeroIndex+1,i)
                    preZeroIndex = i
            cnt += cost(preZeroIndex+1,r)
            return cnt+minVal
        
        ans = 0
        startIndex = 0
        while startIndex < n and diff[startIndex] == 0:
            startIndex += 1

        for i in range(startIndex+1,n):
            if diff[i]*diff[startIndex] >= 0:
                continue
            else:
                # different sign
                ans += cost(startIndex,i)
                startIndex = i
        ans += cost(startIndex,n)
        return ans

