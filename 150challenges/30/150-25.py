class Solution:
    def isPalindrome(self, s: str) -> bool:
        pureString = []
        for item in s:
            if item.isalpha():
                pureString.append(item.lower())
            elif item.isdigit():
                pureString.append(item)
        left = 0
        right = len(pureString)-1
        if right == -1:
            return True
        while left < right:
            if pureString[left] == pureString[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            