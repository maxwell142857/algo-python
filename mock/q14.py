from typing import List
class Solution:
    # brute force,O(n^2)
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     ans = [-1]*n
    #     for i in range(n):
    #         for j in range(1,n):
    #             if nums[(i+j)%n]>nums[i]:
    #                 ans[i] = nums[(i+j)%n]
    #                 break
    #     return ans
    
    # monotonous stack, O(n),from left to right
    # must store (val,index) in stack
    # because we get element's answer when pop element 
    # the order is not guaranteed
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums+nums
        stack = [] # (val,index)
        ans = [-1]*(2*n)
        for i in range(len(nums)):
            while stack and stack[-1][0] < nums[i]:
                element = stack.pop()
                ans[element[1]] = nums[i]
            stack.append((nums[i],i))
        return ans[:n]
    
    # monotonous stack, O(n),from right to left
    # only store val in stack
    # because we get element's answer when push element
    # the order is guaranteed
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums+nums
        stack = [] 
        ans = [-1]*(2*n)
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans[:n]
