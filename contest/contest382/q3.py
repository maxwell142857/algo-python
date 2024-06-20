class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        if n%2 == 0:
            oddN = n//2
        else:
            oddN = n//2+1

        if m%2 == 0:
            oddM = m//2
        else:
            oddM = m//2+1
        
        return oddN*(m-oddM)+oddM*(n-oddN)