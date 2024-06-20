# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

# method1:BFS
# class Codec:

#     def serialize(self, root):
#         if not root:
#             return ''
        
#         level = deque()
#         level.append(root)
#         result = []
#         while level:
#             l = len(level)
#             tmp = []
#             for _ in range(l):
#                 cur = level.popleft()
#                 if cur:
#                     tmp.append(str(cur.val))
#                     level.append(cur.left)
#                     level.append(cur.right)
#                 else:
#                     tmp.append('x')
#             result.append(','.join(tmp))
#         return '!'.join(result)

#     def deserialize(self, data):
#         if not data:
#             return None
        
#         levels = data.split('!')
#         tree = [level.split(',') for level in levels]
#         levelCnt = len(tree)
#         root = TreeNode(tree[0][0])
#         preLevel = [root]
#         for index in range(1,levelCnt-1):
#             # convert this level into node
#             thisL = len(tree[index])
#             level = []
#             for i in range(thisL):
#                 if tree[index][i] != 'x':
#                     level.append(TreeNode(int(tree[index][i])))
#                 else:
#                     level.append(None)
#             preIndex = 0
#             curIndex = 0
#             while curIndex < thisL:
#                 preLevel[preIndex].left = level[curIndex]
#                 curIndex += 1
#                 preLevel[preIndex].right = level[curIndex]
#                 curIndex += 1
#                 preIndex += 1
#             preLevel = [tmp for tmp in level if tmp]
#         return root
        
# method2:DFS, much easier
class Codec:

    def serialize(self, root):
        result = []
        def DFS(cur):
            if not cur:
                result.append(1001) # impossible value
            else:
                result.append(cur.val)
                DFS(cur.left)
                DFS(cur.right)
        DFS(root)
        return ','.join(str(val) for val in result)

    def deserialize(self, data):
        nodes = data.split(',')
        index = 0

        def construct():
            nonlocal index
            if nodes[index] == '1001':
                index += 1
                return None
            
            cur = TreeNode(int(nodes[index]))
            index += 1
            cur.left = construct()
            cur.right = construct()
            return cur

        return construct()
