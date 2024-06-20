class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        half = len(s)//2
        left = s[:half]
        right = s[half:]

        leftPrefix = []
        pre = [0]*26
        leftPrefix.append(pre)
        for i in range(half):
            newLine = list(pre)
            newLine[ord(left[i])-ord('a')] += 1
            leftPrefix.append(newLine)
            pre = newLine

        leftSuffix = []
        pre = [0]*26
        leftSuffix.append(pre)
        for i in range(half):
            newLine = list(pre)
            newLine[ord(left[half-i-1])-ord('a')] += 1
            leftSuffix.append(newLine)
            pre = newLine
        leftSuffix.reverse()

        rightPrefix = []
        pre = [0]*26
        rightPrefix.append(pre)
        for i in range(half):
            newLine = list(pre)
            newLine[ord(right[i])-ord('a')] += 1
            rightPrefix.append(newLine)
            pre = newLine

        rightSuffix = []
        pre = [0]*26
        rightSuffix.append(pre)
        for i in range(half):
            newLine = list(pre)
            newLine[ord(right[half-i-1])-ord('a')] += 1
            rightSuffix.append(newLine)
            pre = newLine
        rightSuffix.reverse()

        ans = []
        for a,b,c,d in queries:
            c -= half
            d -= half

            def arraySubtraction(list1,list2):
                result = []
                for i in range(len(list1)):
                    result.append(list1[i]-list2[i])
                return result
            
            def getInterval(prefix,suffix,l,r):
                result = arraySubtraction(prefix[half],prefix[l])
                result = arraySubtraction(result,suffix[r])
                return result
            
            
            def arraySame(list1,list2):
                for i in range(len(list1)):
                    if list1[i] != list2[i]:
                        return False
                return True
            
            if a > d or b < c:
                # no overlap
                
                leftInterval = getInterval(leftPrefix,leftSuffix,a,b)
                rightInterval = getInterval(rightPrefix,rightSuffix,a,b)
                tmpAns = arraySame(leftInterval,rightInterval)
                leftInterval = getInterval(leftPrefix,leftSuffix,c,d)
                rightInterval = getInterval(rightPrefix,rightSuffix,c,d)
                ans.append(tmpAns and arraySame(leftInterval,rightInterval))
                
            elif a <= c <= d <= b:
                # contain
                pass
            elif c <= a <= b <= d :
                # contain
                pass
            else:
                # overlap

