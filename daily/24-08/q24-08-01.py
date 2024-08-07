class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for d in details:
            age = int(d[12:14])
            if age>60:
                cnt += 1
        return cnt