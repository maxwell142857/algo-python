class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        cnt = 1
        n  = len(s)
        for i in range(1,n):
            if s[i]==s[i-1]:
                cnt += 1
            else:
                if cnt >= 3:
                    ans.append([i-cnt,i-1])
                cnt = 1
        if cnt >= 3:
            ans.append([n-cnt,n-1])
        return ans