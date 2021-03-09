# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if (pHead == None):
            return None
        current = pHead
        while (current != None):
            cloneNode = RandomListNode(current.label)
            nextNode = current.next
            current.next = cloneNode
            cloneNode.next = nextNode
            current = nextNode
        current = pHead
        while (current != None):
            if current.random == None:
                current.next.random = None
            else:
                current.next.random = current.random.next
            current = current.next.next
        current = pHead
        pCloneHead = pHead.next
        while (current != None):
            cloneNode = current.next
            current.next = cloneNode.next
            if cloneNode.next == None:
                cloneNode.next = None
            else:
                cloneNode.next = cloneNode.next.next
            current = current.next
        return pCloneHead
