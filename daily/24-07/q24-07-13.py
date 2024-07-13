class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        n = len(positions)
        for i in range(n):
            robots.append([positions[i],healths[i],directions[i],i])
        robots.sort()
        stack = []
        for robot in robots:
            p,h,d,index = robot
            if d == 'R':
                stack.append([h,d,index])
            else:
                alive = True
                while stack and stack[-1][1] == 'R':
                    if stack[-1][0] < h:
                        stack.pop()
                        h -= 1
                    elif stack[-1][0] == h:
                        stack.pop()
                        alive = False
                        break
                    else:
                        stack[-1][0] -= 1
                        alive = False
                        break
                if alive:
                    stack.append([h,d,index])
        tmp = []
        for r in stack:
            tmp.append([r[2],r[0]])
        tmp.sort()
        ans = []
        for t in tmp:
            ans.append(t[1])
        return ans


