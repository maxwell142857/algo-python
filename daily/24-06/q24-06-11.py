class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0]*len(arr2)
        num2index = { arr2[i]:i for i in range(len(arr2))}
        remain = []
        for num in arr1:
            if num in num2index:
                index = num2index[num]
                cnt[index] += 1
            else:
                remain.append(num)
        ans = []
        for i in range(len(arr2)):
            ans.extend([arr2[i]]*cnt[i])
        
        remain.sort()
        ans.extend(remain)
        return ans

