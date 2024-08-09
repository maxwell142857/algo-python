from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        oddCnt = 0
        for cnt in counter.values():
            if cnt%2:
                oddCnt += 1
                if oddCnt > 1:
                    return False
        return True
