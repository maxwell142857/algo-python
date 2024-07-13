class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def deleteS(s,target):
            c1 = target[0]
            c2 = target[1]
            stack = []
            for c in s:
                if c == c2 and stack and stack[-1] == c1:
                    stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)

        point = 0
        first = 'ab'
        if x<y:
            first = 'ba'
        remain = deleteS(s,first)
        point += (len(s)-len(remain))//2*max(x,y)
        rr = deleteS(remain,first[::-1])
        point += (len(remain)-len(rr))//2*min(x,y)
        
        return point

        
