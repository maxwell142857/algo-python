import heapq as h


class Solution:
    # heap, O(log(n)*k), TLE
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10**9 + 7
        minHeap = []  # [val,index]
        n = len(nums)
        for i in range(n):
            minHeap.append([nums[i], i])
        h.heapify(minHeap)

        for _ in range(k):
            val, index = h.heappop(minHeap)
            val = val * multiplier
            h.heappush(minHeap, [val, index])

        result = [0] * n
        while minHeap:
            val, index = h.heappop(minHeap)
            result[index] = val % MOD
        return result

    # heap+optimization,
    # reference:https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/solutions/5687003/min-heap-greedy/
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10**9 + 7

        def powMod(base, exp):
            result = 1
            while exp:
                if exp & 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp >>= 1
            return result

        # if ignore this edge case, you will get TLE
        if multiplier == 1:
            return nums

        # part1:guarantee everyone gets update
        minHeap = []  # [val,index]
        n = len(nums)
        for i in range(n):
            minHeap.append([nums[i], i])
        h.heapify(minHeap)
        hit = [False] * n
        hitCnt = 0

        while k and hitCnt != n:
            val, index = h.heappop(minHeap)
            val = val * multiplier
            h.heappush(minHeap, [val, index])
            if not hit[index]:
                hit[index] = True
                hitCnt += 1
            k -= 1
        # part2: multiply everyone with avgCnt or avgCnt+1
        result = [0] * n
        avgCnt = k // n
        remain = k - avgCnt * n
        while minHeap:
            val, index = h.heappop(minHeap)
            if remain:
                result[index] = (val % MOD) * powMod(multiplier, avgCnt + 1) % MOD
                remain -= 1
            else:
                result[index] = (val % MOD) * powMod(multiplier, avgCnt) % MOD

        return result
