from sortedcontainers import SortedList
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        BST = SortedList()
        n = len(nums)
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]<nums[i+1]:
                BST.add(i)
        for i in BST.__iter__():
            print(i)
        ans = []
        for t,a,b in queries:
            if t == 1:
                leftIndex = BST.bisect_left(a)
                rightIndex = BST.bisect_right(b)
                cnt = rightIndex-leftIndex-1
                if cnt == -1:
                    ans.append(0)
                else:
                    ans.append(cnt)
            else:
                nums[a] = b
                
                def update(index):
                    if index == 0 or index == n-1:
                        return
                    BST.discard(index)
                    if nums[index]>nums[index-1] and nums[index]<nums[index+1]:
                        BST.add(index)

                for i in range(a-1,a+2):
                    update(i)
        return ans

