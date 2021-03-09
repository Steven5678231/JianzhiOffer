# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.dfs(pRoot) != -1

    def dfs(self, pRoot):
        if pRoot is None:
            return 0
        left = self.dfs(pRoot.left)
        if left == -1:
            return -1
        right = self.dfs(pRoot.right)
        if right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return max(left, right)+1
