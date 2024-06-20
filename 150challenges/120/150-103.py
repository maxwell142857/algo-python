class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()

        def backtracking(path):
            if len(path) == len(nums):
                ans.append(path[:])
            
            for candidate in nums:
                if candidate not in visited:
                    path.append(candidate)
                    visited.add(candidate)
                    backtracking(path)
                    path.pop()
                    visited.remove(candidate)
        
        backtracking([],nums)
        return ans