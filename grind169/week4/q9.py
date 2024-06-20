class Solution:
    # with backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def construct(index):
            if index == len(nums):
                ans.append(path[:])
                return
            
            construct(index+1)

            path.append(nums[index])
            construct(index+1)
            # backtracking
            path.pop()
        
        construct(0)
        return ans


            