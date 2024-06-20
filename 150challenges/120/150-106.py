class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # we difine '(' as 1 and ')' as -1,  the sum < 0 indicates illegal path
        def backtracking(path,sum):
            if len(path) == n*2:
                if sum == 0:
                    ans.append("".join(path))
                return
            if sum < 0:
                return
            
            path.append('(')
            backtracking(path,sum+1)
            path.pop()
            
            path.append(')')
            backtracking(path,sum-1)
            path.pop()
        
        backtracking([],0)
        return ans
    
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # we difine '(' as 1 and ')' as -1,  the sum < 0 indicates illegal path
        def DFS(path,sum):
            if len(path) == n*2:
                if sum == 0:
                    ans.append(path)
                return
            if sum < 0:
                return
            
            DFS(path+'(',sum+1)
            
            DFS(path+')',sum-1)
        
        DFS('',0)
        return ans