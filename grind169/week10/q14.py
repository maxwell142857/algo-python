class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colVal = set()
        diaVal = set()
        reverseDiaVal = set()
        ans = []

        def getAns(path):
            map = []
            
            for index in path:
                curLine = ['.']*n
                curLine[index] = 'Q'
                map.append(''.join(curLine))
            ans.append(map)

        def construct(path):
            newIndex = len(path)
            if newIndex == n:
                getAns(path)
                return
            
            for i in range(n):
                if (i not in colVal) and ((i-newIndex) not in diaVal) and ((i+newIndex) not in reverseDiaVal):
                    path.append(i)
                    colVal.add(i)
                    diaVal.add(i-newIndex)
                    reverseDiaVal.add(i+newIndex)

                    construct(path)

                    path.pop()
                    colVal.remove(i)
                    diaVal.remove(i-newIndex)
                    reverseDiaVal.remove(i+newIndex)

        construct([])
        return ans
        

                
