class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        ansLength = n+1
        ansLeft = 0
        ansRight = n-1
        dictionary = {}
        for item in t:
            dictionary[item] = dictionary.get(item,0)+1
        requiredCnt = len(dictionary)
        currentCnt = 0
        left = 0
        check = {}

        for right in range(n):
            char = s[right]
            if char not in dictionary:
                continue
            check[char] = check.get(char,0)+1
            if check[char] == dictionary[char]:
                currentCnt += 1
                while currentCnt == requiredCnt:
                    char = s[left]
                    if char not in dictionary:
                        left += 1
                        continue
                    check[char] = check.get(char,0)-1
                    if check[char] < dictionary[char]:
                        currentCnt -= 1
                    left += 1
                    # at this time s[left-1:right+1] is the answer
                    if right-left+2 < ansLength:
                        ansLength = right-left+2
                        ansLeft = left-1
                        ansRight = right
        if ansLength != n+1:
            return s[ansLeft:ansRight+1]
        else: 
            return ''
            