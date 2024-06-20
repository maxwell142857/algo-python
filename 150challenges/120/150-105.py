class Solution:
    def totalNQueens(self, n: int) -> int:
        usedCol = set()
        usedDia = set()
        usedSubDia = set()
        ans = 0

        def backtracking(row):
            nonlocal ans
            if row == n:
                ans += 1
                return
            
            for c in range(n):
                if c not in usedCol and row-c not in usedDia and row+c not in usedSubDia:
                    usedCol.add(c)
                    usedDia.add(row-c)
                    usedSubDia.add(row+c)
                    backtracking(row+1)
                    usedCol.remove(c)
                    usedDia.remove(row-c)
                    usedSubDia.remove(row+c)
        
        backtracking(0)
        return ans