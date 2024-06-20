class Solution:
    # the key is to find common prefix

    # ugly
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        def tenToTwo(num):
            if num == 0:
                return [0]
            result = []
            while num:
                result.append(num%2)
                num //= 2
            result.reverse()
            return result


        start = tenToTwo(left)
        end = tenToTwo(right)
        if len(start) != len(end):
            return 0
        else:
            base = 2**(len(start)-1)
            ans = 0
            for i in range(len(start)):
                if start[i] == end[i]:
                    if start[i] == 1:
                        ans += base
                else:
                    break
                base //= 2
            return ans

    # elegant
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left < right:
            left >>= 1
            right >>= 1
            cnt += 1
        return right<<cnt