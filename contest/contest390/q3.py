import heapq
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        num2f = defaultdict(int)
        maxHeap = []
        ans = []
        n= len(nums)
        for i in range(n):
            num = nums[i]
            f = freq[i]
            num2f[num] += f
            heapq.heappush(maxHeap,(-num2f[num],num))
            while maxHeap:
                top = maxHeap[0]
                number = top[1]
                if num2f[number] == -top[0]:
                    # this is a true data
                    ans.append(-top[0])
                    break
                else:
                    # this is a fake data
                    # pop it and find the next
                    heapq.heappop(maxHeap)
            
        return ans