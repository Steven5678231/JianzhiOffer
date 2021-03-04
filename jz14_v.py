# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#

# 快慢指针，一个先走k步，到底了，返回第二个指针，因为相差k步

class Solution:

    def FindKthToTail(self, pHead, k):
        if not pHead:
            return None
        fast, slow = pHead, pHead
        while fast and k > 0:
            fast = fast.next
            k -= 1
        # not long enough
        if k > 0:
            return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        # write code here


solution = Solution()
print(solution.FindKthToTail({1, 2, 3, 4, 5}, 1))
