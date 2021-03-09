# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here\
        hashmap = [0]*256
        for i in s:
            hashmap[ord(i)] += 1
        for i in s:
            if hashmap[ord(i)] == 1:
                return s.index(i)

        return -1


solution = Solution()
print(solution.FirstNotRepeatingChar("google"))
