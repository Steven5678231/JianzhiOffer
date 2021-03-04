# -*- coding:utf-8 -*-
# 反转指针，递归，
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return pHead
        next = pHead.next
        if not next:
            return pHead
        # 先到最底部
        new = self.ReverseList(next)
        # 从底部开始反转，把当前节点设置为后面节点到后续节点
        pHead.next.next = pHead
        pHead.next = None
        return new
