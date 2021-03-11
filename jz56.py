# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead

        new_head = ListNode(-1)
        new_head.next = pHead

        pre = new_head
        currentNode = pHead
        next = None
        while (currentNode != None and currentNode.next != None):
            next = currentNode.next
            if currentNode.val == next.val:
                while next != None and next.val == currentNode.val:
                    next = next.next
                pre.next = next
                currentNode = next
            else:
                pre = currentNode
                currentNode = currentNode.next

        return new_head.next
