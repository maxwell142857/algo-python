from collections import defaultdict
import math
from typing import List


class Solution:
    # TLE
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        if len(coins) == 1 and coins[0] == 1:
            return k
        
        def canMake(num):
            for coin in coins:
                if num%coin == 0:
                    return True
            return False
        cnt = 0
        num = 1
        while cnt !=k:
            if canMake(num):
                cnt += 1
            num += 1
        return num-1
    
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        cnt2lcm = defaultdict(list)
        for i in range(1<<n):
            tmp = []
            cnt = 0
            for index in range(n):
                if (1<<index)&i != 0:
                    tmp.append(coins[index])
                    cnt += 1
            cnt2lcm[cnt].append(math.lcm(*tmp))

        def check(val):
            cnt = 0
            for i in range(1,n+1):
                lcms = cnt2lcm[i]
                for num in lcms:
                    cnt += val//num*pow(-1,i+1)
            return cnt>=k
        
        left = min(coins)
        right = min(coins)*k
        while left < right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left
