class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def lessK(kk):
            num2cnt = defaultdict(int)
            left = 0
            result = 0
            for right in range(n):
                num2cnt[nums[right]] += 1
                while len(num2cnt)==kk:
                    leftNum = nums[left]
                    num2cnt[leftNum] -= 1
                    if num2cnt[leftNum] == 0:
                        del num2cnt[leftNum]
                    left += 1
                result += right-left+1
            return result
        
        return lessK(k+1)-lessK(k)
                    
