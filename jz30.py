# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        f = [0]*len(array)
        if len(array) < 1:
            return 0
        if len(array) < 2:
            return array[0]
        f = [i for i in array]
        for i in range(1, len(array)):
            print(f[i-1]+array[i], array[i])
            f[i] = max(f[i-1]+array[i], array[i])
            print(f[i])
        return max(f)


solution = Solution()
print(solution.FindGreatestSumOfSubArray([1, -2, -3]))
