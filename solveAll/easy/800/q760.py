from collections import defaultdict
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val2indexs = defaultdict(list)
        for i in range(len(nums2)):
            val = nums2[i]
            val2indexs[val].append(i)
        
        ans = []
        for num in nums1:
            ans.append(val2indexs[num].pop())
        return ans