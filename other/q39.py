class Solution:
    # consider i-th candidate, use it or not
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     n = len(candidates)
    #     ans = []
    #     path = []
    #     def construct(index,val):
    #         if val == target:
    #             ans.append(path[:])
    #             return 
    #         if index == n or val > target:
    #             return
            
    #         construct(index+1,val)
    #         path.append(candidates[index])
    #         construct(index,val+candidates[index])
    #         path.pop()
        
    #     construct(0,0)
    #     return ans

    # consider the reversion tree
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        path = []
        def construct(index,val):
            if val == target:
                ans.append(path[:])
                return 
            if val > target:
                return
            
            for i in range(index,n):
                path.append(candidates[i])
                construct(i,val+candidates[i])
                path.pop()
            
        
        construct(0,0)
        return ans