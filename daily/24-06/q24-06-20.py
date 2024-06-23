class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(d):
            pre = -d
            cnt = 0
            for p in position:
                if p-pre >= d:
                    cnt += 1
                    pre = p
            return cnt>=m
        
        # use binary search 
        # TTTFFFF
        left  = 1
        right = max(position)-min(position)
        while left<right:
            mid = (left+right+1)//2
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left
