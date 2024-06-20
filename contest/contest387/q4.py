from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a1 = [nums[0]]
        a2 = [nums[0]]
        array1 = SortedList([nums[0]])
        array2 = SortedList([nums[1]])
        for i in range(2,n):
            cnt1 = count_elements_greater_than_k(array1,nums[i])
            cnt2 = count_elements_greater_than_k(array2,nums[i])
            if cnt1>cnt2:
                array1.add(nums[i])
                a1.append(nums[i])
            elif cnt1<cnt2:
                array2.add(nums[i])
                a2.append(nums[i])
            else:
                if len(array1) <= len(array2):
                    array1.add(nums[i])
                    a1.append(nums[i])
                else:
                    array2.add(nums[i])
                    a2.append(nums[i])
        ans = []
        for num in a1:
            ans.append(num)
        for num in a2:
            ans.append(num)
        return ans


def count_elements_greater_than_k(arr, k):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= k:
            left = mid + 1
        else:
            right = mid
    return len(arr) - left


