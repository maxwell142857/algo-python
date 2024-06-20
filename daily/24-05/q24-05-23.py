from collections import defaultdict
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        visited = defaultdict(int)
        n = len(nums)
        cnt = 0
        def traverse(index):
            nonlocal cnt
            if index == n:
                cnt += 1
                return
            
            # do not use current num
            traverse(index+1)
            # use current num
            if nums[index]-k not in visited and nums[index]+k not in visited:
                visited[nums[index]] += 1
                traverse(index+1)
                visited[nums[index]] -= 1
                if visited[nums[index]] == 0:
                    del visited[nums[index]]
        
        traverse(0)
        return cnt-1 # no-empty subset