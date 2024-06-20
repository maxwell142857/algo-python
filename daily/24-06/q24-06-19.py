class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k>n:
            return -1
        
        def checkDay(d):
            bouquet = 0
            cnt = 0
            for i in range(n):
                if bloomDay[i]<=d:
                    cnt += 1
                    if cnt == k:
                        bouquet += 1
                        cnt = 0
                else:
                    cnt = 0
            return bouquet >=m
        
        # use binary search to check answer
        # FFFFTTTTT,TTTTT,FFFFFF
        left = min(bloomDay)
        right = max(bloomDay)
        while left<right:
            mid = (left+right)//2
            if checkDay(mid):
                right = mid
            else:
                left = mid+1

        if checkDay(right):
            return right
        else:
            return -1
