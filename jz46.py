# -*- coding:utf-8 -*-
# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         res = -1
#         init = range(n)
#         init = init * (n-1)
#         called = []
#         count = 0
#         for i in range(n*(n-1)-1):
#             if (count == m-1):
#                 if init[i] in called:
#                     print("already out", init[i])
#                     continue
#                 else:
#                     print("out", init[i])
#                     called.append(init[i])
#                     count = 0

#             else:
#                 if init[i]not in called:
#                     count += 1
#                     print("not jump:", init[i])
#         print("called", called)
#         for i in range(n-1):
#             if init[i]not in called:
#                 res = init[i]
#                 break
#         return res

class Solution:
    def LastRemaining_Solution(self, n, m):
        if(n == 0):
            return -1
        if (n == 1):
            return 0
        f = [0]*(n+1)
        f[1] = 0
        for i in range(2, n+1):
            f[i] = (f[i-1]+m) % i
            print(i, f[i-1], f[i])
        return f[n]


solution = Solution()
print(solution.LastRemaining_Solution(5, 3))

# range(n)只到n-1
