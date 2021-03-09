# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if (len(pre) == 0):
            return None
        val = pre[0]
        root = TreeNode(val)
        if (len(pre) == 1):
            return root

        rootIndex = tin.index(val)
        print(pre, tin)
        print(rootIndex)
        root.left = self.reConstructBinaryTree(
            pre[1:rootIndex+1], tin[:rootIndex])
        root.right = self.reConstructBinaryTree(
            pre[rootIndex+1:], tin[rootIndex+1:])

        return root


solution = Solution()
print(solution.reConstructBinaryTree(
    [1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7]))
