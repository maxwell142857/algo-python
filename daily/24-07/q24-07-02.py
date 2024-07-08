class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = Counter(nums1)
        ans = []
        for num in nums2:
            if num in hashmap:
                ans.append(num)
                hashmap[num] -= 1
                if hashmap[num] == 0:
                    del hashmap[num]
        return ans