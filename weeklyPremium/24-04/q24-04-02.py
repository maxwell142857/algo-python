class Solution:
    # TLE, O(n^2)
    # def verifyPreorder(self, preorder: List[int]) -> bool:
    #     def verify(start,end):
    #         if start >= end:
    #             return True
    #         breakIndex = -1
    #         rootVal = preorder[start]
    #         for i in range(start+1,end):
    #             if preorder[i]>rootVal:
    #                 breakIndex = i
    #                 break
    #         if breakIndex != -1:
    #             for i in range(breakIndex+1,end+1):
    #                 if preorder[i]<rootVal:
    #                     return False
    #             return verify(start+1,breakIndex-1) and verify(breakIndex,end)
    #         else:
    #             return verify(start+1,end)
    #     return verify(0,len(preorder)-1)

    # # pass, O(n)
    # def verifyPreorder(self, preorder: List[int]) -> bool:
    #     def verify(start,end,lower,upper):
    #         if start > end:
    #             return True
    #         elif start == end:
    #             return lower<preorder[start]<upper
    #         breakIndex = -1
    #         rootVal = preorder[start]
    #         if rootVal>upper or rootVal<lower:
    #             return False
            
    #         for i in range(start+1,end+1):
    #             if preorder[i]>rootVal:
    #                 breakIndex = i
    #                 break
    #         if breakIndex != -1:
    #             return verify(start+1,breakIndex-1,lower,rootVal) and verify(breakIndex,end,rootVal,upper)
    #         else:
    #             return verify(start+1,end,lower,rootVal)
    #     return verify(0,len(preorder)-1,-1,10**4+1)

    # Monotonic Stack
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        minVal = -1
        for val in preorder:
            if val < minVal:
                return False
            while stack and stack[-1] < val:
                minVal = stack.pop()
            stack.append(val)
        return True