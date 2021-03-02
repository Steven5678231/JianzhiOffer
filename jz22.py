# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        currentStack = [root]
        res = []
        while currentStack:
            nextStack = []
            for node in currentStack:
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
                res.append(node.val)
            currentStack = nextStack

        return res


solution = Solution()
solution.PrintFromTopToBottom(1)

# 每层遍历节点，添加进queue
