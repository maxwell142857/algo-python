import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []
        visited = set()
        cnt = 0
        l1 = len(nums1)
        l2 = len(nums2)
        heap.append((nums1[0]+nums2[0],0,0))
        visited.add((0,0))
        while heap:
            current = heapq.heappop(heap)
            ans.append((nums1[current[1]],nums2[current[2]]))
            cnt += 1
            if cnt == k:
                break
            if (current[1]+1,current[2]) not in visited and current[1]+1 < l1:
                sum = nums1[current[1]+1]+nums2[current[2]]
                heapq.heappush(heap,(sum,current[1]+1,current[2]))
                visited.add((current[1]+1,current[2]))
            if (current[1],current[2]+1) not in visited and current[2]+1 < l2:
                sum = nums1[current[1]]+nums2[current[2]+1]
                heapq.heappush(heap,(sum,current[1],current[2]+1))
                visited.add((current[1],current[2]+1))

        return ans
            
