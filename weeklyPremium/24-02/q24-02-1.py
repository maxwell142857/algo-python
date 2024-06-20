class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        def flip(index):
            result = list(currentState[::])
            result[index] = '-'
            result[index+1] = '-'
            return ''.join(result)
        
        n = len(currentState)
        ans = []
        for i in range(n-1):
            if currentState[i] == currentState[i+1]=='+':
                ans.append(flip(i))
        return ans
