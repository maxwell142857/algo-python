class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(i,mid,j):
            arr1 = nums[i:mid]
            arr2 = nums[mid:j]
            n1,n2 = len(arr1),len(arr2)
            p,p1,p2 = i,0,0
            while p1 < n1 and p2 < n2:
                if arr1[p1]<arr2[p2]:
                    nums[p] = arr1[p1]
                    p1 += 1
                else:
                    nums[p] = arr2[p2]
                    p2 += 1
                p += 1
            while p1 < n1:
                nums[p] = arr1[p1]
                p1 += 1
                p += 1
            
            while p2 < n2:
                nums[p] = arr2[p2]
                p2 += 1
                p += 1


            
        def sort(i,j):
            if i+1>=j:
                return
            
            mid = (i+j)//2
            sort(i,mid)
            sort(mid,j)
            merge(i,mid,j)

        sort(0,len(nums))
        return nums
            

            
