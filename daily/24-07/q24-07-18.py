# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        def distance2leaves(node):
            nonlocal ans
            if not node:
                return []
            
            leftResult = distance2leaves(node.left)
            rightResult = distance2leaves(node.right)
            if not leftResult and not rightResult:
                return [0]
            elif not leftResult:
                return [num+1 for num in rightResult]
            elif not rightResult:
                return [num+1 for num in leftResult]
            else:
                for i in leftResult:
                    for j in rightResult:
                        if i+j <= distance-2:
                            ans += 1
                return [num+1 for num in rightResult]+[num+1 for num in leftResult]
        
        distance2leaves(root)
        return ans

    # optimize by count sort, as distance <= 10
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        def distance2leaves(node):
            nonlocal ans
            cnt = [0]*distance
            
            if not node:
                return cnt
            if not node.left and not node.right:
                cnt[0] = 1
                return cnt
            
            leftResult = distance2leaves(node.left)
            rightResult = distance2leaves(node.right)
            # update ans
            for i in range(distance):
                for j in range(distance):
                    if i+j+2<=distance:

                        ans += leftResult[i]*rightResult[j]

            for i in range(1,distance):
                cnt[i] += leftResult[i-1]
                cnt[i] += rightResult[i-1]

            return cnt

            
        
        distance2leaves(root)
        return ans

            
            