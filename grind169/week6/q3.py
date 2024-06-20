from collections import Counter
import heapq
class Node:
    def __init__(self,f,s) -> None:
        self.f = f
        self.s = s
    def __lt__(self,other):
        if self.f != other.f:
            return self.f<other.f
        else:
            return self.s>other.s
    def __str__(self) -> str:
        return f'MyClass(value={self.s})'
class Solution:
    # O(n*log(n))
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     word2f = defaultdict(int)
    #     for word in words:
    #         word2f[word] += 1
    #     array  =[]
    #     for key,val in word2f.items():
    #         array.append([val,key])
    #     array.sort(key=lambda x: (-x[0], x[1]))
    #     ans = []
    #     for i in range(k):
    #         ans.append(array[i][1])
    #     return ans

    # O(n*log(k))
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []
        for key,val in cnt.items():
            heapq.heappush(heap,Node(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).s)
        return ans[::-1]