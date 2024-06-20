class Solution:
    # DFS without memo, TLE
    # def findRotateSteps(self, ring: str, key: str) -> int:
    #     n = len(ring)
    #     char2index = defaultdict(list)
    #     for i in range(len(ring)):
    #         char2index[ring[i]].append(i)
       
    #     ans = float('inf')
    #     def DFS(bias,pKey,cost):
    #         nonlocal ans
    #         if pKey == len(key):
    #             ans = min(ans,cost)
    #             return 
            
    #         indexs = char2index[key[pKey]]
    #         for index in indexs:
    #             trueIndex = (index+bias)%n
    #             distance = min(n-trueIndex,trueIndex)
    #             DFS(n-index,pKey+1,cost+distance)
        
    #     DFS(0,0,0)
    #     return ans+len(key)
    
    # DFS with memo, 
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        char2index = defaultdict(list)
        for i in range(len(ring)):
            char2index[ring[i]].append(i)
       
        memo = [[-1]*len(key) for _ in range(n)]
        def DFS(bias,pKey):
            if pKey == len(key):
                return 0 
            
            if memo[bias][pKey] != -1:
                return memo[bias][pKey]
            
            ans = float('inf')
            indexs = char2index[key[pKey]]
            for index in indexs:
                trueIndex = (index+bias)%n
                distance = min(n-trueIndex,trueIndex)
                result = DFS((n-index)%n,pKey+1)
                ans = min(ans,result+distance)

            memo[bias][pKey] = ans
            return ans
        
        return DFS(0,0)+len(key)


        
        