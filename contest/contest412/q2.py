class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def check(val1,val2):
            if val1 == val2:
                return True
                
            # change val1
            s1 = str(val1)
            s1 = [c for c in s1]
            l1 = len(s1)
            for i in range(l1):
                for j in range(i+1,l1):
                    s1[i],s1[j] = s1[j],s1[i]
                    if int(''.join(s1)) == val2:
                        return True
                    s1[i],s1[j] = s1[j],s1[i]
            
            # change val2
            s2 = str(val2)
            s2 = [c for c in s2]
            l2 = len(s2)
            for i in range(l2):
                for j in range(i+1,l2):
                    s2[i],s2[j] = s2[j],s2[i]
                    if int(''.join(s2)) == val1:
                        return True
                    s2[i],s2[j] = s2[j],s2[i]
            
            return False

        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if check(nums[i],nums[j]):
                    cnt += 1
        return cnt