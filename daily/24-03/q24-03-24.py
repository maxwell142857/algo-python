class Solution:
    # sort the array, O(n*log(n))
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
    # bit mask, O(n*log(n))
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)+1
        bitL = n.bit_length()
        ans = 0
        for i in range(bitL):
            mask = 1<<i
            cnt1 = 0
            cnt2 = 0
            for j in range(1,n+1):
                if mask&j:
                    cnt1 += 1
            
            for num in nums:
                if mask&num:
                    cnt2 += 1
            if cnt2>cnt1:
                ans |= mask
        return ans
    
    # slow and fast pointer, O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break
        
        fast = nums[0]
        while fast!=slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return fast
    
    # mark index, O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            val = abs(num)
            if nums[val-1] < 0:
                return val
            else:
                nums[val-1] = -nums[val-1]
        
        return 0
    
    # cycle sort, O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        p = 0
        while p < n:
            val = nums[p]
            if nums[val-1] != val:
                nums[val-1],nums[p] = nums[p],nums[val-1]
            else:
                if p == val-1:
                    p += 1
                else:
                    return val
        return 0
            