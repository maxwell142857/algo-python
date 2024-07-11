class Node:
    def __init__(self,val) -> None:
        self.next = None
        self.val = val
class Solution:
    # simulation, O(n^2)
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        head = Node(-1)
        p = head
        for i in range(1,n+1):
            node = Node(i)
            p.next = node
            p = p.next
        p.next = head.next

        p = head.next
        while p.next != p:
            for _ in range(k-2):
                p = p.next
            p.next = p.next.next
            p = p.next
        return p.val

    # math+recursion,O(n)
    def findTheWinner(self, n: int, k: int) -> int:
        def calculate(cnt):
            if cnt == 1:
                return 0
            else:
                return (calculate(cnt-1)+k)%cnt
        return calculate(n)+1
