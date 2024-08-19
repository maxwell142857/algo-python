from collections import Counter
class Solution:
    # backtracking + set, O(2^n), TLE
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = set()
        def choose(index,val,path):
            if index == n:
                return
            
            # do not use current number
            choose(index+1,val,path)

            # use current number
            path.append(candidates[index])
            val -= candidates[index]

            if val == 0:
                ans.add(tuple(path))
            else:
                choose(index+1,val,path)
            path.pop()
        
        choose(0,target,[])
        listAns = []
        for l in ans:
            listAns.append(list(l))
        return listAns
    
    # backtracking, use counter to avoid dumplication
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        valAndCnt = [] # [val,cnt]
        for k,v in counter.items():
            valAndCnt.append([k,v])
        valAndCnt.sort()
        n = len(valAndCnt)
        ans = []
        path = []
        def choose(index,remain):
            if remain == 0:
                ans.append(path[:])
                return 
            if index == n or remain < 0:
                return
            
            val,cnt = valAndCnt[index]
            for i in range(cnt+1):
                remain -= val*i
                for _ in range(i):
                    path.append(val)

                choose(index+1,remain)

                for _ in range(i):
                    path.pop()
                remain += val*i
        choose(0,target)
        return ans


