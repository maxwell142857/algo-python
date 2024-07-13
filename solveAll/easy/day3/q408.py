class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n1,n2 = len(word),len(abbr)
        p1,p2 = 0,0
        number = 0
        while True:
            if p1>=n1 or p2>=n2:
                return p1==n1 and p2==n2
            
            if abbr[p2].isalpha():
                if word[p1] == abbr[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    return False
            else:
                val = int(abbr[p2])
                if number==0 and val==0:
                    return False
                number = number*10+val
                if (p2 == n2-1) or abbr[p2+1].isalpha():
                    p1 += number
                    number = 0
                p2 += 1
