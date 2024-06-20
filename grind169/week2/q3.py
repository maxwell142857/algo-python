class Solution:
    # space complexity:O(n)
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []
        for char in s:
            if char != '#':
                sStack.append(char)
            else:
                if sStack:
                    sStack.pop()
        for char in t:
            if char != '#':
                tStack.append(char)
            else:
                if tStack:
                    tStack.pop()
        
        while sStack and tStack:
            if sStack.pop() != tStack.pop():
                return False
        
        return not sStack and not tStack
    
     # space complexity:O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        sPointer = len(s)-1
        tPointer = len(t)-1
        sDelete = 0
        tDelete = 0
        while True:
            while sPointer>=0:
                if s[sPointer] == '#':
                    sPointer -= 1
                    sDelete += 1
                else:
                    if sDelete > 0:
                        sDelete -= 1
                        sPointer -= 1
                    else:
                        break
            while tPointer>=0:
                if t[tPointer] == '#':
                    tPointer -= 1
                    tDelete += 1
                else:
                    if tDelete > 0:
                        tDelete -= 1
                        tPointer -= 1
                    else:
                        break
            if sPointer < 0 and tPointer < 0:
                return True
            elif sPointer < 0 or tPointer < 0:
                return False
            else:
                if s[sPointer] != t[tPointer]:
                    return False
                else:
                    sPointer -= 1
                    tPointer -= 1
            
                
