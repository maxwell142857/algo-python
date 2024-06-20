class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s1 = list(a)
        s1.reverse()
        s2 = list(b)
        s2.reverse()
        pointer = 0
        l1 = len(s1)
        l2 = len(s2)
        ans = []
        pre = 0
        while True:
            if pointer < l1 and pointer < l2:
                sum = int(s1[pointer])+int(s2[pointer])+pre
            elif pointer < l1:
                sum = int(s1[pointer])+pre
            elif pointer < l2:
                sum = int(s2[pointer])+pre
            else:
                break
            pre = 0
            if sum >= 2:
                sum -= 2
                pre = 1
            ans.append(sum)
            pointer += 1

        if pre:
            ans.append(1)
        ans.reverse()
        return ''.join(map(str, ans))