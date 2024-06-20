class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        def addToK(k):
            ans = 0
            if cost1*2 > cost2:
                # use operation2 is cheaper
                diff = [k-num for num in nums if k-num != 0]
                diff.sort()
                l = len(diff)
                left = 0
                right = l-1
                while left<right:
                    diff[left] -= 1
                    diff[right] -= 1
                    ans += cost2
                    if diff[left]==0:
                        left += 1
                    if diff[right]==0:
                        right -= 1
                if left==right:
                    ans += diff[left]*cost1
                            
            else:
                # use operation1 for all
                for num in nums:
                    ans += (k-num)*cost1
            return ans
        
        val = max(nums)
        return min(addToK(val),addToK(val+1))
