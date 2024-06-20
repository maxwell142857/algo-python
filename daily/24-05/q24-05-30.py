class Solution:
    # enumerate j ,and the span from j to left and right
    # O(n^2)
    # def countTriplets(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     cnt = 0
    #     for j in range(1,n):
    #         # left[:j]
    #         # right[j:]
    #         val2cnt = defaultdict(int)
    #         tmp = 0
    #         for index in range(j-1,-1,-1):
    #             tmp = tmp^arr[index]
    #             val2cnt[tmp] += 1
    #         tmp = 0
    #         for index in range(j,n):
    #             tmp = tmp^arr[index]
    #             cnt += val2cnt[tmp]
            
    #     return cnt

    # math+preSum
    # math: ^[i, j) = ^[j, k] -> (^[i, j)) ^ (^[j, k]) = 0 -> find ^[i,k] = 0
    # O(n)
    def countTriplets(self, arr: List[int]) -> int:
        val2cnt = defaultdict(list)
        tmp = 0
        cnt = 0
        n = len(arr)
        val2cnt[0].append(-1)
        for index in range(n):
            val = arr[index]
            tmp = tmp^val
            indexs = val2cnt[tmp]
            for ii in indexs:
                cnt += index-ii-1
            indexs.append(index)

        return cnt