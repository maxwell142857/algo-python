from collections import Counter


class Solution:
    # use set
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        candidates = []
        path = []
        used = set()
        n = len(nums)
        def DFS():
            if len(path) == n:
                candidates.append(tuple(path))
            for i in range(n):
                if i not in used:
                    path.append(nums[i])
                    used.add(i)
                    DFS()
                    path.pop()
                    used.remove(i)
        DFS()
        return list(set(candidates))
    
    # use counter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        candidates = []
        path = []
        n = len(nums)
        counter = Counter(nums)
        def DFS():
            if len(path) == n:
                candidates.append(path[:])
            for key,val in counter.items():
                if val > 0:
                    path.append(key)
                    counter[key] -= 1
                    DFS()
                    path.pop()
                    counter[key] += 1

        DFS()
        return candidates