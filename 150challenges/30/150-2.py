from typing import List

def removeElement(nums: List[int], val: int) -> int:
    total = len(nums)
    cnt = 0
    index = 0
    while index < len(nums):
        if nums[index] == val:
            cnt += 1
            del nums[index]
        else:
            index += 1
    print(nums)
    print(cnt)
    return total-cnt



removeElement([0,1,2,2,3,0,4,2],2)