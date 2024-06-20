class Solution:
    # O(n*lg(n)) binary search
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            result = Bsearch(numbers,i+1,n-1,target-numbers[i])
            if result != -1:
                return [i+1,result+1]
            
    # O(n) two pointer
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1
def Bsearch(numbers,left,right,target):
    while left <= right:
        mid = (left+right)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1