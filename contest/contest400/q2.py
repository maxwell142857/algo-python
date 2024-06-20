class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        def overlap(a,b):
            if a[0]>b[1] or a[1]<b[0]:
                return False
            else:
                return True
        def merge(a,b):
            return [min(a[0],b[0]),max(a[1],b[1])]
        n = len(meetings)
        cur = meetings[0]
        p = 1
        ans = days
        while p < n:
            if overlap(cur,meetings[p]):
                cur = merge(cur,meetings[p])
                p += 1
            else:
                ans -= (cur[1]-cur[0]+1)
                cur = meetings[p]
                p += 1
            
        ans -= (cur[1]-cur[0]+1)
        return ans
