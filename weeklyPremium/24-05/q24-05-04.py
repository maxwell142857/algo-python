class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        l1 = len(pattern)
        l2 = len(s)
        c2s = {}
        s2c = {}
        result = False
        def traverse(index1,index2):
            nonlocal result
            if index1 == l1 and index2 == l2:
                result = True
                return
            
            if index1 == l1 or index2 == l2:
                return
            
            c = pattern[index1]
            if c in c2s:
                target = c2s[c]
                l = len(target)
                if index2+l<=l2 and s[index2:index2+l] == target:
                    traverse(index1+1,index2+l)
                else:
                    return
            else:
                for end in range(index2+1,l2+1):
                    sub = s[index2:end]
                    if sub not in s2c:
                        c2s[c] = sub
                        s2c[sub] = c
                        traverse(index1+1,end)
                        del c2s[c]
                        del s2c[sub]
                    else:
                        continue
        
        traverse(0,0)
        return result
                    
