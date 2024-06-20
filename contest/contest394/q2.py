class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mySet = {}
        for i in range(len(word)):
            c = word[i]
            if 'a'<=c<='z':
                # record the last index
                mySet[c] = i
            else:
                # record the last index
                if c not in mySet:
                    mySet[c] = i
        cnt = 0
        for i in range(26):
            low = chr(ord('a')+i)
            upper = chr(ord('A')+i)
            if low in mySet and upper in mySet and mySet[low]<mySet[upper]:
                cnt += 1
        return cnt