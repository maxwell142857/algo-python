class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = [c for c in s]

        n = len(s)
        pH,pT = 0,n-1
        while pH<pT:
            while pH < n and not s[pH].isalpha():
                pH += 1
            while pT >= 0 and not s[pT].isalpha():
                pT -= 1

            if pH>=pT:
                break
            result[pH],result[pT] = result[pT],result[pH]
            pH += 1
            pT -= 1
        return ''.join(result)

        
        
        
