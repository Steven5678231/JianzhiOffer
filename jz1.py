# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array)-1
        cols = len(array[0])-1
        i = rows
        j = 0
        while (i >= 0) and (j <= cols):
            if (target < array[i][j]):
                i -= 1
            elif (target > array[i][j]):
                j += 1
            else:
                return True

        return False


solution = Solution()
print(solution.Find(
    7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))

# def Find(self, target, array):
#     for arr in array:
#         try:
#             i = arr.index(target)
#         except:
#             i = -1

#         if (i != -1):
#             return True
#     return False
