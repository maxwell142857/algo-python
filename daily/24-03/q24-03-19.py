import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task2cnt = defaultdict(int)
        for task in tasks:
            task2cnt[task] += 1
        heap = [] # (-cnt,lastDealTime)
        for val in task2cnt.values():
            heapq.heappush(heap,[-val,-n-1])
        
        timeSlot = 0
        while heap:
            dont = []
            while heap and timeSlot-heap[0][1]<=n:
                dont.append(heapq.heappop(heap))
            if heap:
                target = heapq.heappop(heap)
                target[0] += 1
                if target[0] != 0:
                    target[1] = timeSlot
                    dont.append(target)
            timeSlot += 1
            for tmp in dont:
                heapq.heappush(heap,tmp)
        return timeSlot
