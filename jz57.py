# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if (pNode.right != None):
            pRight = pNode.right
            while pRight.left != None:
                pRight = pRight.left
            return pRight

        pParent = pNode.next
        if pParent == None:
            return None
        while pParent.right == pNode and pParent.next != None:
            pNode = pParent
            pParent = pNode.next
        if pParent.next == None and pParent.right == pNode:
            return None
        return pParent
