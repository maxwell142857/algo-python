class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        tmp = []
        def construct(index,val):
            if val == 0:
                ans.append(tmp[:])
                return
            if val < 0:
                return
            if index == n:
                return
            
            construct(index+1,val)
            
            val -= candidates[index]
            tmp.append(candidates[index])
            construct(index,val)
            val += candidates[index]
            tmp.pop()

        construct(0,target)
        return ans
        
    # dfs
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        tmp = []
        
        def DFS(index,val):
            if val == target:
                ans.append(tmp[:])
                return
            if val > target:
                return
            
            for i in range(index,n):
                tmp.append(candidates[i])
                DFS(i,val+candidates[i])
                tmp.pop()
        DFS(0,0)
        return ans
        