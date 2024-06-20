class Solution:
    # O(n^2) although use sort+BSearch, the del in list is O(n)
    # def numRescueBoats(self, people: List[int], limit: int) -> int:
    #     people.sort()
    #     cnt = 0
    #     while people:
    #         first = people[0]
    #         left = 0
    #         right = len(people)-1
    #         while left < right:
    #             mid = (left+right+1)//2
    #             if people[mid]+first<=limit:
    #                 left = mid
    #             else:
    #                 right = mid-1
    #         if left == 0:
    #             del people[0]
    #         else:
    #             del people[left]
    #             del people[0]
    #         cnt+= 1
    #     return cnt

    # O(n*lgn),sort+ two pointers
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        cnt = 0
        while left < right:
            if people[left]+people[right]>limit:
                right -= 1
            else:
                left += 1
                right -= 1
            cnt += 1
        if left == right:
            cnt += 1
        return cnt
            