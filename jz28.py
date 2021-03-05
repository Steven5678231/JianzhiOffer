# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        threshold = len(numbers)/2
        sortedlist = sorted(numbers)
        print(sortedlist)
        start = 0
        while start < len(sortedlist)-1:
            count = 1
            next = sortedlist[start+1]

            while next and sortedlist[start] == next and start+2 < len(sortedlist):
                start += 1
                count += 1
                next = sortedlist[start+1]
            if count > threshold:
                return sortedlist[start-1]

            start += 1
        return 0


solution = Solution()
print(solution.MoreThanHalfNum_Solution([1, 2, 3, 2, 4, 2, 5, 2, 3]))

# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         l = len(numbers)
#         for i in numbers:
#             if numbers.count(i)>(l/2):
#                 return i
#         return 0
