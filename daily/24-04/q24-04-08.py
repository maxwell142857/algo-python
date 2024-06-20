from collections import deque,Counter
class Solution:
    # simulation
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        myDeque = deque(students)
        cnt = Counter(students)
        p = 0
        while p < n:
            if (cnt[0]==0 and sandwiches[p]==0) or (cnt[1]==0 and sandwiches[p]==1):
                return len(myDeque)
            student = myDeque.popleft()
            if student == sandwiches[p]:
                p += 1
                cnt[student] -= 1
            else:
                myDeque.append(student)
            
        return 0
    
    # count, more simple
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        n = len(sandwiches)
        for i in range(n):
            cur = sandwiches[i]
            if cnt[cur] == 0:
                return n-i
            else:
                cnt[cur] -= 1
        return 0