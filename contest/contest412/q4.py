class Solution:
    #  O(n^2),TLE
    def countPairs(self, nums: List[int]) -> int:

        def check(val1,val2):
            if val1 == val2:
                return True

            digits1 = []
            digits2 = []
            while val1 or val2:
                if val1:
                    digits1.append(val1%10)
                    val1 //= 10
                else:
                    digits1.append(0)
                
                if val2:
                    digits2.append(val2%10)
                    val2 //= 10
                else:
                    digits2.append(0)
            diff1,diff2 = [],[]
            for i in range(len(digits1)):
                if digits1[i] != digits2[i]:
                    diff1.append(digits1[i])
                    diff2.append(digits2[i])

            if len(diff1) == 1 or len(diff1)>4:
                return False
            if len(diff1) in [2,3]:
                diff1.sort()
                diff2.sort()
                for i in range(len(diff1)):
                    if diff1[i] != diff2[i]:
                        return False
                return True
            else:
                # len(diff) = 4
                # s1 = f'{diff1[0]}{diff1[1]}{diff1[2]}{diff1[3]}'
                s1 = f'{diff1[1]}{diff1[0]}{diff1[3]}{diff1[2]}'
                s2 = f'{diff1[2]}{diff1[3]}{diff1[0]}{diff1[1]}'
                s3 = f'{diff1[3]}{diff1[2]}{diff1[1]}{diff1[0]}'
                sOther =  f'{diff2[0]}{diff2[1]}{diff2[2]}{diff2[3]}'
                if sOther in [s1,s2,s3]:
                    return True
                else:
                    return False
        
        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if check(nums[i],nums[j]):
                    cnt += 1
                    # print(nums[i],nums[j])
        return cnt

    # O(n*d^4),where d is the length of number
    def countPairs(self, nums: List[int]) -> int:
        pow10 = [1]
        digitCnt = 9
        for _ in range(digitCnt-1):
            pow10.append(pow10[-1]*10)
        

        def allOneSwapVariations(val):
            result = set()
            
            for i in range(digitCnt):
                for j in range(i+1,digitCnt):
                    di = val//pow10[i]%10
                    dj = val//pow10[j]%10
                    mutation = val+(dj-di)*pow10[i]+(di-dj)*pow10[j]
                    result.add(mutation)
            return result

        def allTwoSwapVariations(val):
            oneResult = allOneSwapVariations(val)
            result = set()
            for r in oneResult:
                result |= allOneSwapVariations(r)
            return result
        
        val2cnt = defaultdict(int)
        ans = 0
        for val in nums:
            mutations = allTwoSwapVariations(val)
            for m in mutations:
                ans += val2cnt[m]
            val2cnt[val] += 1
        return ans


