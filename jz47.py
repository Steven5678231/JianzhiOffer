# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        # 短路and判断0，递归结束
        ans = n
        temp = ans and self.Sum_Solution(n-1)
        ans = ans+temp
        return ans
# 递归取代+
# and取代if
