class Solution:
    # hashmap+ sorting
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        array = []
        for val,cnt in count.items():
            array.append([val,cnt])
        array.sort()
        n = len(array)
        ans = 0
        for i in range(n-1):
            if array[i+1][0]-array[i][0] == 1:
                ans = max(ans,array[i+1][1]+array[i][1])

        return ans
    
    # hashmap without sorting
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for key in count.keys():
            if key+1 in count.keys():
                ans = max(ans,count[key]+count[key+1])
        return ans