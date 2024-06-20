class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        maxL = 0
        for length in range(1,n):
            if word[:length] == word[-length:] and (n-length)%k==0:
                maxL = length

        deleteCnt = n-maxL
        if deleteCnt == 0:
            return 1
        else:
            ans = deleteCnt//k
            if deleteCnt%k!=0:
                ans += 1
            return ans
