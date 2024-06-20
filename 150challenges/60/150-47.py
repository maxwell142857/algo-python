class Solution:
    # ugly one
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        start2end = {}
        end2start = {}
        ans = 0
        for item in nums:
            result = insert(start2end,end2start,item)
            ans = max(ans,result)
        return ans
    
    # clever one
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for item in nums:
            if item-1 not in nums:
                end = item+1
                while end in nums:
                    end += 1
                ans = max(ans,end-item)
        return ans


                
def insert(start2end,end2start,value):
    if value+1 in start2end and value-1 in end2start:
        # merge to left and right
        end = start2end[value+1]
        start = end2start[value-1]
        start2end[start] = end
        end2start[end] = start
        del start2end[value+1]
        del end2start[value-1]
        return end-start+1
    elif value+1 in start2end:
        # merge to right
        end = start2end[value+1]
        start2end[value] = end
        end2start[end] = value
        del start2end[value+1]
        return end-value+1
    elif value-1 in end2start:
        #merge to left
        start = end2start[value-1]
        start2end[start] = value
        end2start[value] = start
        del end2start[value-1]
        return value-start+1
    else:
        # do nothing
        start2end[value] = value
        end2start[value] = value
        return 1