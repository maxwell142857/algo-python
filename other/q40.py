class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        val2cnt = Counter(candidates)
        numbers = [[number,cnt] for number,cnt in val2cnt.items() if number <=target]

        def construct(index,val):
            if val == target:
                ans.append(path[:])
                return 
            if val > target:
                return
            
            for i in range(index,len(numbers)):
                number,cnt = numbers[i]
                if cnt > 0:
                    
                    path.append(number)
                    numbers[i][1] -= 1
                    construct(i,val+number)
                    path.pop()
                    numbers[i][1] += 1
            
        
        construct(0,0)
        return ans