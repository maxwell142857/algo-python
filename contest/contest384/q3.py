class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        lengths = []
        pairCnt = 0
        singleCnt = 0
        char2cnt = {}
        for word in words:
            lengths.append(len(word))
            for char in word:
                char2cnt[char] =  char2cnt.get(char,0)+1
        
        for value in char2cnt.values():
            if value%2!=0:
                singleCnt += 1
            pairCnt += value//2

        lengths.sort()
        ans = 0
        for length in lengths:
            pairNeed = length//2
            if length%2 == 1:
                singleNeed = 1
            else:
                singleNeed = 0
            # check whether can satisfy
            if pairCnt-pairNeed>=0 and singleCnt-singleNeed>=0:
                pairCnt -= pairNeed
                singleCnt -= singleNeed
                ans += 1
            elif pairCnt-pairNeed>=1 and singleCnt-singleNeed==-1:
                pairCnt -= pairNeed+1
                singleCnt = 1
                ans += 1
            else:
                break
        return ans