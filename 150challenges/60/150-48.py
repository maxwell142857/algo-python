class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n= len(nums)
        if n == 0:
            return []
        start = nums[0]
        ans = []
        
        for i in range(1,n):
            if nums[i]!= nums[i-1]+1:
                if start != nums[i-1]:
                    ans.append(f"{start}->{nums[i-1]}") 
                else:
                    ans.append(str(start))
                start = nums[i]
        #deal the last group
        if start != nums[n-1]:
            ans.append(f"{start}->{nums[n-1]}") 
        else:
            ans.append(str(start))
        return ans