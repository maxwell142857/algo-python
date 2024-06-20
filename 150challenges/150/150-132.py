class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1
        addOne = False
        while index >= 0:
            digits[index] += 1
            if digits[index] == 10:
                digits[index] = 0
                addOne = True
                index -= 1
            else:
                addOne = False
                break
        if addOne:
            digits.insert(0,1)
        return digits