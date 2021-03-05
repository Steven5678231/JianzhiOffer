# -*- coding:utf-8 -*-
# set 可以去重
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]

        res = []
        print(ss)
        for i in range(len(ss)):
            for substr in self.Permutation(ss[:i]+ss[i+1:]):
                res.append(ss[i]+substr)
        return (sorted(list(set(res))))


solution = Solution()
print(solution.Permutation("ab"))

# library
# import itertools
# class Solution:
#     def Permutation(self, ss):
#         # write code here
#         if not ss:
#             return []
#         return sorted(list(set(map(''.join, itertools.permutations(ss)))))
