class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = set()

        def DFS():
            if len(used) == len(nums):
                ans.append(path[:])
                return
            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)
                    DFS()
                    path.pop()
                    used.remove(num)
        
        DFS()
        return ans