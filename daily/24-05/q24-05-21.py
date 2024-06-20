class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def DFS(index):
            if index == n:
                ans.append(path[:])
                return
            
            DFS(index+1)

            path.append(nums[index])
            DFS(index+1)
            path.pop()
        
        DFS(0)
        return ans
                