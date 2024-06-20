class Solution:
    # wrong solution, treat [1,2],[2,1] the same
    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     def findCnt(index,val):
    #         if val == 0:
    #             return 1
    #         if index == n:
    #             return 0
    #         way = 0
    #         curCnt = 0
    #         while val-curCnt*nums[index]>=0:
    #             way += findCnt(index+1,val-curCnt*nums[index])
    #             curCnt += 1
    #         return way
        
    #     return findCnt(0,target)
    
    # order matter
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = [-1]*(target+1)
        def findCnt(val):
            if val == 0:
                return 1
            if memo[val] !=-1:
                return memo[val]
            
            way = 0
            for i in range(n):
                if val-nums[i]>=0:
                    way += findCnt(val-nums[i])
            memo[val] = way      
            return memo[val]
        
        return findCnt(target)
