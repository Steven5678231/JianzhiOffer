# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # min = Math.min(pHead2.val, pHead1.val)
        phead = ListNode(0)
        start = phead
        while pHead1 or pHead2:
            if not pHead1:
                phead.next = pHead2
                return start.next
            if not pHead2:
                phead.next = pHead1
                return start.next
            if (pHead1.val < pHead2.val):
                phead.next = pHead1
                phead = phead.next
                pHead1 = pHead1.next
            else:
                phead.next = pHead2
                phead = phead.next
                pHead2 = pHead2.next
# 递归版本 速度快很多且内存占用减少


def Merge(self, pHead1, pHead2):
    if (pHead1 == None):
        return pHead2
    if (pHead2 == None):
        return pHead1
    if (pHead1.val < pHead2.val):
        pHead1.next = self.Merge(pHead1.next, pHead2)
        return pHead1
    else:
        pHead2.next = self.Merge(pHead1, pHead2.next)
        return pHead2
