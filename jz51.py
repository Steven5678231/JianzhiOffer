# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        total = 1
        for i in A:
            total *= i
        result = [1]*len(A)

        for i in range(1, len(A)):
            result[i] = result[i-1]*A[i-1]
        temp = 1
        for j in range(len(A)-2, -1, -1):
            print(temp, j, result[j])
            temp *= A[j+1]
            result[j] *= temp
        return result


solution = Solution()
print(solution.multiply([1, 2, 3, 4, 5]))
