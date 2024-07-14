class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [] # (element,cnt)
        n = len(formula)
        p = 0
        char = ''
        cnt = 0
        while p<n:
            c = formula[p]
            if not c.isnumeric() and char:
                stack.append([char,1])
                char = ''

            if c.isalpha():
                char = c
                p += 1
                while p<n and formula[p].islower():
                    char += formula[p]
                    p += 1
            elif c.isnumeric():
                cnt = int(c)
                p += 1
                while p<n and formula[p].isnumeric():
                    cnt *= 10
                    cnt += int(formula[p])
                    p += 1
                stack.append([char,cnt])
                char = ''
                cnt = 0
            elif c == '(':
                p += 1
                stack.append('(')
            elif c == ')':
                cnt = 0
                p += 1
                while p<n and formula[p].isnumeric():
                    cnt *= 10
                    cnt += int(formula[p])
                    p += 1
                if cnt == 0:
                    cnt = 1
                tmp = []
                while stack[-1] != '(':
                    cur = stack.pop()
                    tmp.append([cur[0],cur[1]*cnt])
                stack.pop() # remove (
                for t in tmp:
                    stack.append(t)
            else:
                pass
        if char:
            stack.append([char,1])
        # calculate
        name2cnt = defaultdict(int)
        for e,number in stack:
            name2cnt[e] += number
        
        result = []
        for k,v in name2cnt.items():
            result.append((k,v))
        result.sort()
        
        ans = []
        for r in result:
            ans.append(r[0])
            if r[1]>1:
                ans.append(str(r[1]))
        return ''.join(ans)

            