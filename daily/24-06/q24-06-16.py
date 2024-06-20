class Solution:
    # suppose all number can cover [1,a)
    # after add a missing x, can cover [1,a) and [x,a+x)
    # since x<=a
    # so can cover [1,a+x)
    # so the greater x be, the better
    # so x = a
    # so when the range only cover [1,a), add a to let it cover [1,2a)
    def minPatches(self, nums: List[int], n: int) -> int:
        nextRight = 1
        l = len(nums)
        p = 0
        cnt = 0
        while nextRight <= n:
            if p < l:
                if nums[p] <= nextRight:
                    nextRight += nums[p]
                    p += 1
                else:
                    cnt += 1
                    nextRight *= 2
            else:
                cnt += 1
                nextRight *= 2
        return cnt

