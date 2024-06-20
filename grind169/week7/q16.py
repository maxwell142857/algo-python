# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursion back, O(n^2)
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     cnt = 0
    #     def DFS(node):
    #         nonlocal cnt
    #         if not node:
    #             return []
    #         result = []
    #         if node.left:
    #             left = DFS(node.left)
    #             for num in left:
    #                 result.append(num+node.val)
    #                 if num+node.val == targetSum:
    #                     cnt += 1
    #         if node.right:
    #             right = DFS(node.right)
    #             for num in right:
    #                 result.append(num+node.val)
    #                 if num+node.val == targetSum:
    #                     cnt += 1
    #         result.append(node.val)
    #         if node.val == targetSum:
    #             cnt += 1
    #         return result
    #     DFS(root)
    #     return cnt

    # DFS in DFS, O(n^2)
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     cnt = 0
    #     def DFS(node):
    #         if not node:
    #             return
    #         test(node,0)
    #         DFS(node.left)
    #         DFS(node.right)

    #     def test(node,val):
    #         nonlocal cnt
    #         val += node.val
    #         if val == targetSum:
    #             cnt += 1
    #         if node.left:
    #             test(node.left,val)
    #         if node.right:
    #             test(node.right,val)

    #     DFS(root)
    #     return cnt
    
    # DFS with preSum, O(n)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        preSum = defaultdict(int)
        preSum[0] = 1
        cnt = 0

        def DFS(node,val):
            nonlocal cnt

            if not node:
                return
            
            val += node.val
            cnt += preSum[val-targetSum]
            preSum[val] += 1
            DFS(node.left,val)
            DFS(node.right,val)
            preSum[val] -= 1
        
        DFS(root,0)
        return cnt
