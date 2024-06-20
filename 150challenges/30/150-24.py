
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordIndex = 0
        ans = []
        wordCnt = len(words)
        currentLine = []
        currentCharCnt = 0
        while wordIndex < wordCnt:
            if currentCharCnt == 0:
                currentLine.append(words[wordIndex])
                currentCharCnt = len(words[wordIndex])
            elif currentCharCnt+1+len(words[wordIndex]) <= maxWidth:
                currentLine.append(words[wordIndex])
                currentCharCnt = currentCharCnt+1+len(words[wordIndex])
            else:
                ans.append(justify(currentLine,maxWidth))
                currentLine = []
                currentCharCnt = len(words[wordIndex])
                currentLine.append(words[wordIndex])
            wordIndex += 1
        # the last line
        lastLine = currentLine[0]
        for lastIndex in range(1,len(currentLine)):
            lastLine += ' '+ currentLine[lastIndex]
        spaceCnt = maxWidth-len(lastLine)
        lastLine += ' '*spaceCnt
        ans.append(lastLine)
        return ans

def justify(currentLine,maxWidth):
        wordCnt = len(currentLine)
        if wordCnt == 1:
            ans = currentLine[0]
            ans += ' '*(maxWidth-len(currentLine[0]))
            return ans
        spaceRemain = maxWidth
        for item in currentLine:
            spaceRemain -= len(item)
        spaceCnt = wordCnt-1
        space = [spaceRemain//spaceCnt]*spaceCnt
        spaceRemain -= (spaceRemain//spaceCnt)*spaceCnt
        index = 0
        while(spaceRemain>0):
            space[index] += 1
            spaceRemain -= 1
            index += 1
        ans = currentLine[0]
        for i in range(1,wordCnt):
            ans += ' '*space[i-1]
            ans += currentLine[i]
        return ans

s = Solution()
s.fullJustify(["Listen","to","many,","speak","to","a","few."],6)