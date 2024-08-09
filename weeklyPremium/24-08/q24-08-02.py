class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # key:(r1,c1,r2,c2) which means (r3,c3) between (r1,c1) and (r2,c2)
        # val: (r3,c3)
        checkBetween = {} 
        checkBetween[(0,0,0,2)] = (0,1)
        checkBetween[(0,0,2,0)] = (1,0)
        checkBetween[(0,0,2,2)] = (1,1)
        checkBetween[(0,2,0,0)] = (0,1)
        checkBetween[(0,2,2,2)] = (1,2)
        checkBetween[(0,2,2,0)] = (1,1)
        checkBetween[(2,0,0,0)] = (1,0)
        checkBetween[(2,0,0,2)] = (1,1)
        checkBetween[(2,0,2,2)] = (2,1)
        checkBetween[(2,2,0,0)] = (1,1)
        checkBetween[(2,2,0,2)] = (1,2)
        checkBetween[(2,2,2,0)] = (2,1)
        checkBetween[(0,1,2,1)] = (1,1)
        checkBetween[(2,1,0,1)] = (1,1)
        checkBetween[(1,0,1,2)] = (1,1)
        checkBetween[(1,2,1,0)] = (1,1)

        def validInK(k):
            result = 0
            
            
            def DFS(r,c,cnt):
                nonlocal result

                cnt += 1

                if cnt == k:
                    result += 1
                    return
                
                for i in range(3):
                    for j in range(3):
                        if used[i][j]:
                            continue
                        if (r,c,i,j) in checkBetween:
                            midR,midC = checkBetween[(r,c,i,j)]
                            if not used[midR][midC]:
                                continue
                        used[i][j] = True
                        DFS(i,j,cnt)
                        used[i][j] = False

            for i in range(3):
                for j in range(3):
                    used = [[False]*3 for _ in range(3)]
                    used[i][j] = True
                    DFS(i,j,0)
                    used[i][j] = False
            return result

        ans = 0
        for i in range(m,n+1):
            ans += validInK(i)
        return ans