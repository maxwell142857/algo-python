class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def construct(path):
            if len(path) == n:
                ans.append(path)
                return
            
            if not path:
                construct('1')
                construct('0')
            else:
                if path[-1] == '1':
                    construct(path+'1')
                    construct(path+'0')
                else:
                    construct(path+'1')
        construct('')
        return ans


                
