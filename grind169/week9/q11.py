class Solution:
    # preSum
    # for using i-th height, size = heights[i]*(lessRight[i]-lessLeft[i]-1)
    # O(n)
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     n = len(heights)
    #     lessLeft = [-1]*n
    #     for i in range(1,n):
    #         p = i-1
    #         while p>=0 and heights[p]>=heights[i]:
    #             p = lessLeft[p]
    #         lessLeft[i] = p

    #     lessRight = [n]*n
    #     for i in range(n-1,-1,-1):
    #         p = i+1
    #         while p<n and heights[p] >= heights[i]:
    #             p = lessRight[p]
    #         lessRight[i] = p
        
    #     ans = 0
    #     for i in range(n):
    #         ans = max(ans,heights[i]*(lessRight[i]-lessLeft[i]-1))
        
    #     return ans

    # Divide and Conquer
    # This approach relies on the observation that the rectangle with maximum area will be the maximum of:
    # The widest possible rectangle with height equal to the height of the shortest bar.
    # The largest rectangle confined to the left of the shortest bar(subproblem).
    # The largest rectangle confined to the right of the shortest bar(subproblem).
    # average O(n*lgn), worst O(n^2)
    # TLE
    # if you want, optimize by segment tree
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     def getSize(left,right):
    #         if left > right:
    #             return 0
            
    #         minIndex = left
    #         minHeight = heights[left]
    #         for i in range(left,right+1):
    #             if heights[i]<minHeight:
    #                 minHeight = heights[i]
    #                 minIndex = i
    #         return max(minHeight*(right-left+1),getSize(left,minIndex-1),getSize(minIndex+1,right))
        
    #     return getSize(0,len(heights)-1)
    






    # this method's thought is same as method1 preSum
    # however it uses monotonous stack instead of preSum to get Left and right in O(n)

    # Idea is, we will consider every element a[i] to be a candidate for the area calculation. 
    # That is, if a[i] is the minimum element then what is the maximum area possible for all such rectangles? 
    # We can easily figure out that it's a[i]*(R-L+1-2) or a[i] * (R-L-1)
    # where a[R] is first subsequent element(R>i) in the array just smaller than a[i]
    # similarly a[L] is first previous element just smaller than a[i].
    # But how to implement it efficiently?

    # We add the element a[i] directly to the stack if it's greater than the peak element (or a[i-1] )
    # because we are yet to find R for this. 
    # L is just the previous element in stack

    # What if we get an element a[i] which is smaller than the peak value
    # it is the R value for all the elements present in stack which are greater than a[i]
    # Pop out the elements greater than a[i], we have their R value and L value. 

    # mono stack
    # O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        stack = [(0,-1)] # (val,index)
        ans = 0
        for i in range(n):
            while stack and stack[-1][0]>heights[i]:
                val,index = stack.pop()
                rightIndex = i # exclude
                leftIndex = stack[-1][1] # exclude
                height = val
                ans = max(ans,height*(rightIndex-leftIndex-1))
            stack.append((heights[i],i))
        return ans
                
        