class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        array = []
        for k,v in cnt.items():
            array.append((k,v))

        array.sort(key = lambda x:(x[1],-x[0]))
        ans = []
        for val,cnt in array:
            for _ in range(cnt):
                ans.append(val)
        return ans