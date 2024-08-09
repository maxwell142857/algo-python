class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        length = 0
        lineCnt = 0
        for c in s:
            if length + widths[ord(c)-ord('a')] <= 100:
                length += widths[ord(c)-ord('a')]
            else:
                lineCnt += 1
                length = widths[ord(c)-ord('a')]
        return [lineCnt+1,length]
            
