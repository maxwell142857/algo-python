class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        n = len(word)
        p = 0
        while p < n:
            cur = word[p]
            end = p+1
            while end<n and word[end]==cur:
                end += 1
            cnt = end-p
            while cnt > 9:
                result.append(str(9))
                result.append(cur)
                cnt -= 9
            result.append(str(cnt))
            result.append(cur)
            p = end
        
        return ''.join(result)
