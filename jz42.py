# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        end = len(array)-1
        res = 10000000
        head = 0
        tmpres = []
        while head < end:
            tmp = array[head]+array[end]
            while tmp > tsum:
                end -= 1
                tmp = array[head]+array[end]
                print(head, end, tmp)
                if end < head:
                    break
            while tmp < tsum:
                head += 1
                tmp = array[head]+array[end]
                print(head, end, tmp)
                if head > end:
                    break

            if tmp == tsum:
                print(head, end, tmp)
                if (array[head]*array[end] < res):
                    res = array[head]*array[end]
                    tmpres = [array[head], array[end]]
                head += 1
                end -= 1

        return tmpres


solution = Solution()
print(solution.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
