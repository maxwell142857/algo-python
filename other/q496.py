class Solution:
    # brute force, O(m*n)
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     n  = len(nums1)
    #     ans = []
    #     for target in nums1:
    #         find = False
    #         add = False
    #         for num in nums2:
    #             if find:
    #                 if num > target:
    #                     ans.append(num)
    #                     add = True
    #                     break
    #             else:
    #                 if num == target:
    #                     find = True
    #         if not add:
    #             ans.append(-1)
    #     return ans
    
    # O(n) monotonous stack, from right to left
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     stack = []
    #     val2index = {}
    #     for i in range(len(nums1)):
    #         val2index[nums1[i]] = i
    #     ans = [-1]*len(nums1)

    #     for i in range(len(nums2)-1,-1,-1):
    #         while stack and stack[-1] <= nums2[i]:
    #             stack.pop()
    #         if stack and nums2[i] in val2index:
    #             ans[val2index[nums2[i]]] = stack[-1]
    #         stack.append(nums2[i])
    #     return ans

    # O(n) monotonous stack, from left to right
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        val2index = {}
        for i in range(len(nums1)):
            val2index[nums1[i]] = i
        ans = [-1]*len(nums1)

        for i in range(len(nums2)):
            while stack and stack[-1] <= nums2[i]:
                val = stack.pop()
                if val in val2index:
                    ans[val2index[val]] = nums2[i]
            stack.append(nums2[i])
        return ans
