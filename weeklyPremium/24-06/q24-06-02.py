class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        common = set(arrays[0])
        cnt = len(arrays)
        for i in range(1,cnt):
            cur = set(arrays[i])
            common = common&cur
        common = list(common)
        common.sort()
        return common