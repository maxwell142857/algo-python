class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        n = len(low)
        charArray = []
        for i in range(n):
            if low[i].isalpha() or low[i].isnumeric():
                charArray.append(low[i])
        
        if not charArray:
            return True
        
        left = 0
        right = len(charArray)-1
        while left<right and charArray[left]==charArray[right]:
            left += 1
            right -= 1
        return left >= right