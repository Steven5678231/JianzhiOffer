# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        f = [0]*(number+1)
        f[1] = 1
        for i in range(number+1):
            if i == number:
                f[i] = 1
            else:
                f[i] = i
            for j in range(i+1):
                f[i] = max(f[i], f[i-j]*f[j])
        return f[number]


solution = Solution()
print(solution.cutRope(8))
