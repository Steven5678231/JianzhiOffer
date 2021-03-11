# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    result = []

    def Print(self, pRoot):
        # write code here
        node = pRoot
        queue = []
        queue.append(node)
        while (queue != None):
            currentqueue = queue
            new_queue = []
            new_result = []
            while (currentqueue != None):
                node = currentqueue.pop()
                new_result.append(node.val)
                if node.left != None:
                    new_queue.append(node.left)
                if node.right != None:
                    new_queue.append(node.right)
            self.result.append(new_result)
            queue = new_queue
        return self.result


solution = Solution()
print(solution.Print({8, 6, 10, 5, 7, 9, 11}))
