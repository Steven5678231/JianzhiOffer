# -*- coding:utf-8 -*-
# 如果n大于0，直接计算即可，如果n小于0，计算2的32次方加上n的结果中1的个数。
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        total = 0
        neg = n < 0
        if n < 0:
            n = n & 0xffffffff

        while (n > 0):
            tmp = n % 2
            n /= 2
            if tmp == 1:
                count += 1
            total += 1
#         if neg:
#             count = total- count +1
        return count

# -*- coding:utf-8 -*-


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while (n != 0):
            n = n & (n-1)
            count += 1
        return count
