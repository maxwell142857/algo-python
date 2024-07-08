class Solution:
    # trie + dfs, TLE
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = {}
        for i,w in enumerate(words):
            p = trie
            for c in w:
                if c not in p:
                    p[c] = {}
                p = p[c]
            if '!' not in p:
                p['!'] = costs[i]
            else:
                p['!'] = min(p['!'],costs[i])
        
        n = len(target)
        ans = float('inf')

        def construct(index,cost):
            nonlocal ans
            if cost>ans:
                return
            p = trie
            while index < n and target[index] in p:
                p = p[target[index]]
                index += 1
                if '!' in p:
                    if index == n:
                        ans = min(ans,cost+p['!'])
                        return
                    else:
                        construct(index,cost+p['!'])
        
        construct(0,0)
        if ans == float('inf'):
            return -1
        return ans
    
    # trie + dp
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = {}
        for i,w in enumerate(words):
            p = trie
            for c in w:
                if c not in p:
                    p[c] = {}
                p = p[c]
            if '!' not in p:
                p['!'] = costs[i]
            else:
                p['!'] = min(p['!'],costs[i])
        
        n = len(target)
        dp = [0]*n # infinite for impossible, 0 for unknown

        def construct(index):
            if dp[index] != 0:
                return dp[index]
            
            curIndex = index
            ans = float('inf')
            p = trie
            while index < n and target[index] in p:
                p = p[target[index]]
                index += 1
                if '!' in p:
                    if index == n:
                        ans =  min(ans,p['!'])
                    else:
                        ans = min(ans,construct(index)+p['!'])
            
            dp[curIndex] = ans
            return dp[curIndex]
                        
        
        construct(0)
        if dp[0] == float('inf'):
            return -1
        else:
            return dp[0]
                

