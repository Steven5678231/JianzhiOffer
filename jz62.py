# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        result = []

        def dfs(pRoot):
            print(result)
            if pRoot.left != None:
                dfs(pRoot.left)
            result.append(pRoot.val)
            if pRoot.right != None:
                dfs(pRoot.right)
        if pRoot == None:
            return None
        dfs(pRoot)
        return result[k]
