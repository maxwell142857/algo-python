from collections import deque
class Solution:
    # O(n^2)
    # def numSteps(self, s: str) -> int:
    #     number = [int(c) for c in s]
    #     number = deque(number[::-1])
    #     cnt = 0
    #     while len(number) != 1:
    #         if number[0] == 0:
    #             number.popleft()
    #         else:
    #             for i in range(len(number)):
    #                 number[i] += 1
    #                 if number[i]==2:
    #                     number[i] = 0
    #                     add = 1
    #                 else:
    #                     add = 0
    #                     break
    #             if add:
    #                 number.append(1)
    #         cnt += 1
        
    #     if number[0] == 0:
    #         return cnt+1
    #     else:
    #         return cnt
    

    # O(n)
    def numSteps(self, s: str) -> int:
        n = len(s)
        carry = 0
        cnt = 0
        for p in range(n-1,0,-1):
            if int(s[p])+carry == 0:
                cnt += 1
                carry = 0
            elif int(s[p])+carry == 1:
                cnt += 2
                carry = 1
            else:
                cnt += 1
                carry = 1
        if carry:
            cnt += 1
        return cnt
