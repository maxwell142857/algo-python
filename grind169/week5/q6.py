class Solution:
    # brute force, O(n^2)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        for i in range(n):
            cur = temperatures[i]
            nextt = i+1
            while nextt < n:
                if temperatures[nextt]>cur:
                    ans[i] = nextt-i
                    break
                nextt += 1
        return ans
    
    # O(n*100)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        t2lastIndex = {}
        for i in range(n-1,-1,-1):
            cur = temperatures[i]
            nextt = n+1
            for j in range(cur+1,101):
                if j in t2lastIndex:
                    nextt = min(nextt,t2lastIndex[j])
            if nextt!=n+1:
                ans[i] = nextt-i
            t2lastIndex[cur] = i
        return ans
