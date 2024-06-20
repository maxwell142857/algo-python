class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total  = sum(apple)
        capacity.sort(reverse = True)
        cnt = 0
        mySum = 0
        while mySum < total:
            mySum += capacity[cnt]
            cnt += 1
        return cnt
