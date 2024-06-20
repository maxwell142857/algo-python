import heapq as h
class Solution:
    def clearStars(self, s: str) -> str:
        minHeap = [] # (char,-index) # delete 'a' before 'b'. When choosing 'a',choose the one with max index
        delIndex = set()
        n = len(s)
        for i in range(n):
            if s[i] == '*':
                delIndex.add(i)
                if minHeap:
                    cur = h.heappop(minHeap)
                    delIndex.add(-cur[1])
            else:
                h.heappush(minHeap,(ord(s[i])-ord('a'),-i))
        result = []
        for i in range(n):
            if i not in delIndex:
                result.append(s[i])

        return ''.join(result)

        