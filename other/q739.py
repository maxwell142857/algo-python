class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = [] #(val,index)
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                element = stack.pop()
                ans[element[1]] = i-element[1]
            stack.append((temperatures[i],i))
        return ans