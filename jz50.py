# -*- coding:utf-8 -*-

class Solution:
    def duplicate(self, numbers):
        n = len(numbers)
        found = []
        for i in numbers:
            if i in found:
                return i
            else:
                found.append(i)
        return -1


solution = Solution()
print(solution.duplicate([2, 3, 1, 0, 2, 5, 3]))

# 替换
# class Solution:
#     def duplicate(self , numbers ):
#         # write code here
#         if not numbers:
#             return -1
#         for i in range(len(numbers)):
#             if i != numbers[i]:
#                 if numbers[i] == numbers[numbers[i]]:
#                 # 说明已经被占位了，比如numbers[4]=2,numbers[2]=2
#                     return numbers[i]

#                 tmp = numbers[i]
#                 numbers[i] = numbers[numbers[i]]
#                 numbers[tmp] = tmp
#         return -1
