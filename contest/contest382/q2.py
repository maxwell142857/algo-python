class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # deal with 1
        oneCnt = 0
        num2cnt = {}
        for number in nums:
            if number == 1:
                oneCnt += 1
            else:
                num2cnt[number] = num2cnt.get(number,0)+1
        
        if oneCnt%2 == 0:
            ans = oneCnt-1
        else:
            ans = oneCnt
            
        candidates = set(sorted(nums))
        for candidate in candidates:
            cnt = 0
            current = candidate
            while num2cnt.get(current,0) >= 2:
                cnt += 1
                current = current**2
            if num2cnt.get(current,0) == 1:
                ans = max(ans,cnt*2+1)
            else:
                ans = max(ans,cnt*2-1)
        return ans

