class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mySet = set()
        for c in word:
            mySet.add(c)
        cnt = 0
        for i in range(26):
            low = chr(ord('a')+i)
            upper = chr(ord('A')+i)
            if low in mySet and upper in mySet:
                cnt += 1
        return cnt
                