class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        # left is 1 and right is -1, we must guarantee val >=0
        def generate(path,val):
            if len(path) == 2*n:
                if val == 0:
                    ans.append(''.join(path))
                return
            
            if val < n:
                path.append('(')
                generate(path,val+1)
                path.pop()
            if val > 0:
                path.append(')')
                generate(path,val-1)
                path.pop()
        
        generate([],0)
        return ans
