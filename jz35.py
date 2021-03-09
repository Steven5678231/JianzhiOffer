# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        temp = [0] * len(data)

        def mergeSort(l, r):
            if r-l <= 1:
                return 0
            mid = (r+l)/2
            ans = mergeSort(l, mid)+mergeSort(mid, r)
            temp[l:r] = data[l:r]
            i, j = l, mid
            for k in range(l, r):


solution = Solution()
print(solution.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
