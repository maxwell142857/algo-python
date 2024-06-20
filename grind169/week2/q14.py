# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(start,end):
            if start == end:
                return TreeNode(nums[start])
            elif start > end:
                return None
            else:
                mid = (start+end)//2
                node = TreeNode(nums[mid])
                node.left = construct(start,mid-1)
                node.right = construct(mid+1,end)
                return node
            
        return construct(0,len(nums)-1)