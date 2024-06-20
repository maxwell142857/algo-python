class Solution:
    # recursion+preDeal,O(n)
    def decodeString(self, s: str) -> str:
        char = 'abcdefghijklmnopqrstuvwxyz'
        left2right = {} # find the index of ],query by index of [
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '[':
                stack.append(i)
            elif s[i] == ']':
                leftIndex = stack.pop()
                left2right[leftIndex] = i
        
        def solve(cnt,start,end):
            result = ''
            curCnt = 0
            p = start
            while p < end+1:
                if s[p] in char:
                    result += s[p]
                    p += 1
                elif s[p] == '[':
                    # find the ]
                    index = left2right[p] # index of ]
                    result += solve(curCnt,p+1,index-1)
                    curCnt = 0
                    p = index+1
                elif s[p] == ']':
                    p += 1
                else:
                    curCnt *= 10
                    curCnt += int(s[p])
                    p += 1
            return result*cnt
        
        return solve(1,0,n-1)

    # stack, O(n)
    def decodeString(self, s: str) -> str:
        stack = []
        char = 'abcdefghijklmnopqrstuvwxyz'

        times = 0
        result = ''
        for c in s:
            if c.isdigit():
                times *= 10
                times += int(c)
            elif c in char:
                if not stack:
                    result += c
                else:
                    stack.append(c)
            elif c == '[':
                stack.append(str(times))
                times = 0
            else:
                # c = ']'
                tmpS= []
                while not stack[-1].isdigit():
                    tmpS.append(stack.pop())
                
                tmpS = tmpS[::-1]*int(stack.pop())
                if not stack:
                    result += ''.join(tmpS)
                else:
                    for tmpC in tmpS:
                        stack.append(tmpC)
        return result

            
            
