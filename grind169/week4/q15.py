class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number2char = [ \
            ['0'],['1'],['a','b','c'],['d','e','f'],\
            ['g','h','i'],['j','k','l'],['m','n','o'],\
            ['p','q','r','s'],['t','u','v'],['w','x','y','z'],\
            ]
        ans = []
        def backtracking(index,path):
            if index == len(digits):
                if path:
                    ans.append(''.join(path))
                return
            
            charSet = number2char[int(digits[index])]
            for char in charSet:
                path.append(char)
                backtracking(index+1,path)
                path.pop()
        
        backtracking(0,[])
        return ans