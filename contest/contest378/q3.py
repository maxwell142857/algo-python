class Solution:
    def maximumLength(self, s: str) -> int:
        s += '!'
        ans = -1
        for i in range(26):
            target = chr(ord('a')+i)
            length2cnt = {}
            length = 0
            index = 0
            for index in range(len(s)):
                if s[index] == target:
                    length += 1
                else:
                    if length != 0:
                        length2cnt[length] = length2cnt.get(length,0)+1
                        if length-1 > 0:
                            length2cnt[length-1] = length2cnt.get(length-1,0)+2
                        if length-2 > 0:
                            length2cnt[length-2] = length2cnt.get(length-2,0)+3
                        length = 0
            for key,val in length2cnt.items():
                if val >= 3:
                    ans = max(ans,key)
        return ans
    
s = Solution()
print(s.maximumLength("aaaa"))
                