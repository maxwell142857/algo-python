class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        mid = (left+right)//2
        while left < right:
            mid = (left+right+1)//2
            if check(citations,mid):
                left = mid
            else:
                 right = mid-1
        return left
    





def check(citation,h):
        cnt = 0
        for item in citation:
            if item >= h:
                cnt += 1
        return cnt >= h    