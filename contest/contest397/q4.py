from typing import List
class Solution:
    # brute force with pruning
    # O(n!)
    # calculate value during backtracking
    # if calculate value at leave node will cost O(n),get TLE
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        path = []
        used = set()
        minScore = float('inf')
        ans = nums[:]

        def backtracking(tmp):
            nonlocal ans,minScore
            
            # pruning here
            if len(path)>=2:
                tmp += abs(path[-2]-nums[path[-1]])
                if tmp >= minScore:
                    return
                
            if len(path)==n:
                score = tmp+abs(path[n-1]-nums[path[0]])
                if score < minScore:
                    minScore = score
                    ans = path[:]
                return
            
            for i in range(n):
                if i not in used:
                    used.add(i)
                    path.append(i)
                    backtracking(tmp)
                    used.remove(i)
                    path.pop()
        
        backtracking(0)
        return ans