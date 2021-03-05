# -*- coding:utf-8 -*-
# @param s string字符串
# @return string字符串
#
class Solution:
    def replaceSpace(self, s):
        # write code here
        if len(s) == 0:
            return ""
        print(s, len(s))
        ch = s[0]
        if len(s) == 1:
            if ch == " ":
                return "%20"
            else:
                return ch
        else:
            if ch == " ":
                return "%20"+self.replaceSpace(s[1:])
            else:
                return ch+self.replaceSpace(s[1:])


solution = Solution()
print(solution.replaceSpace("We Are Happy"))

# class Solution:
#     def replaceSpace(self, s):
#         return s.replace(" ","%20")
