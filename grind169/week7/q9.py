from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            if not stack:
                stack.append(aster)
            else:
                if aster > 0:
                    stack.append(aster)
                else:
                    while stack and stack[-1] > 0 and stack[-1] < -aster:
                        stack.pop()
                    if not stack:
                        stack.append(aster)
                        continue
                    if stack[-1] < 0:
                        stack.append(aster)
                    else:
                        if stack[-1] == -aster:
                            stack.pop()
                        else:
                            # aster is destroyed
                            pass
        return stack
