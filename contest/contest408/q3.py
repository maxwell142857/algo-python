from collections import deque
class Solution:
    # O(n^2), brute force,TLE
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for start in range(n):
            cnt0 = 0
            cnt1 = 0
            for end in range(start+1,n):
                if s[end] == '1':
                    cnt1 += 1
                else:
                    cnt0 += 1
                if cnt1>=cnt0*cnt0:
                    ans += 1
        return ans
    
    # O(n^(3/2)), sliding windows
    def numberOfSubstrings(self, s: str) -> int:
        # can not run sliding windows directly
        # subquestion: fix the number of 0, run sliding windows
        n = len(s)
        maxZero = 0
        while maxZero*maxZero+maxZero <= n:
            maxZero += 1

        ans = 0
        for zeroCnt in range(maxZero):
            zeroIndex = deque()
            left = 0
            curZeroCnt = 0
            minL = zeroCnt*zeroCnt+zeroCnt

            for right in range(n):
                if s[right] == '0':
                    curZeroCnt += 1
                    zeroIndex.append(right)
                while curZeroCnt > zeroCnt:
                    if s[left] == '0':
                        curZeroCnt -= 1
                        zeroIndex.popleft()
                    left += 1

                if curZeroCnt == zeroCnt and minL <= right-left+1:
                    leadingZeroIndex = right
                    if zeroIndex:
                        leadingZeroIndex = zeroIndex[0]
                    # how many leading 1 you can delete
                    # first, based on leadingZeroIndex
                    # also need to satisfy minL <= length
                    toIndex = min(leadingZeroIndex,right-minL+1)
                    ans += toIndex-left+1
            print(zeroCnt,ans)
        return ans

