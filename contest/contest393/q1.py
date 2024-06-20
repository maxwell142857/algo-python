class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = []
        if s[0] == '?' and s[1] == '?':
            ans.append('1')
            ans.append('1')
        elif s[0] == '?':
            if s[1] == '0' or s[1] == '1':
                ans.append('1')
            else:
                ans.append('0')
            ans.append(s[1])
        elif s[1] == '?':
            ans.append(s[0])
            if s[0] == '1':
                ans.append('1')
            else:
                ans.append('9')
        else:
            ans.append(s[0])
            ans.append(s[1])
        
        ans.append(':')

        if s[3] == '?':
            ans.append('5')
        else:
            ans.append(s[3])
        
        if s[4] == '?':
            ans.append('9')
        else:
            ans.append(s[4])
        return ''.join(ans)