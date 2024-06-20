class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        mySet = Counter(nums1)

        def check(x):
            hashmap = defaultdict(int)
            for num in nums2:
                hashmap[num-x] += 1
            delta = 0
            for key,val in hashmap.items():
                if key in mySet and mySet[key]>=val:
                    continue
                else:
                    return False
            return True
        
        # find min ans
        for ans in range(-1000,1001):
            if check(ans):
                return ans
        return 0
