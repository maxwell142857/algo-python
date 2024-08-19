import heapq as h
class Solution:
    # brute force, TLE
    def nthUglyNumber(self, n: int) -> int:
        def isUgly(val):
            while val%5==0:
                val //= 5
            while val%3==0:
                val //= 3
            while val%2==0:
                val //= 2
            return val == 1
        
        cnt = 0
        val = 1
        while True:
            if isUgly(val):
                cnt += 1
            if cnt == n:
                return val

            val += 1
    
    # merge n sorted list
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        cnt = 0
        preVal = -1
        while True:
            curVal = h.heappop(minHeap)
            if curVal != preVal:
                cnt += 1
                if cnt == n:
                    return curVal
                h.heappush(minHeap, curVal*2)
                h.heappush(minHeap, curVal*3)
                h.heappush(minHeap, curVal*5)
            preVal = curVal
        