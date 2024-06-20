class Solution:
    # preSum
    # time: O(n)
    # space: O(n)
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     leftHeight = [0]*n
    #     leftHeight[0] = 0
    #     for i in range(1,n):
    #         leftHeight[i] = max(leftHeight[i-1],height[i-1])

    #     rightHeight = [0]*n
    #     rightHeight[n-1] = 0
    #     for i in range(n-2,-1,-1):
    #         rightHeight[i] = max(rightHeight[i+1],height[i+1])
        
    #     ans = 0
    #     for i in range(n):
    #         cur = min(leftHeight[i],rightHeight[i])-height[i]
    #         if cur > 0:
    #             ans += cur
    #     return ans
        
    # two pointer
    # time: O(n)
    # space: O(1)
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1
        leftMax = 0
        rightMax = 0
        while left<=right:
            if leftMax>rightMax:
                # move right pointer
                if rightMax < height[right]:
                    rightMax = height[right]
                else:
                    ans += rightMax-height[right]
                right -= 1
            else:
                # move left pointer
                if leftMax<height[left]:
                    leftMax = height[left]
                else:
                    ans += leftMax-height[left]
                left += 1
        return ans
