class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number2letter = {}
        number2letter[2] = 'abc'
        number2letter[3] = 'def'
        number2letter[4] = 'ghi'
        number2letter[5] = 'jkl'
        number2letter[6] = 'mno'
        number2letter[7] = 'pqrs'
        number2letter[8] = 'tuv'
        number2letter[9] = 'wxyz'
        ans = []

        def DFS(index,path):
            nonlocal ans
            if index == len(digits):
                ans.append("".join(path))
                return

            candidate = number2letter[int(digits[index])]
            for letter in candidate:
                path.append(letter)
                DFS(index+1,path)
                path.pop()
        if digits != "":
            DFS(0,[])
        return ans

