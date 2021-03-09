# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        # 蒂姆排序
        # tinput.sort()

        def quick_sort(input):
            if not input:
                return []
            pivot = input[0]
            left = quick_sort([x for x in input[1:] if x < pivot])
            right = quick_sort([x for x in input[1:] if x > pivot])
            return left + [pivot] + right

        def select_sort(input):
            if not input:
                return []
            for i in range(len(input)):
                smallest = i
                for j in range(i, len(input)):
                    if input[j] < input[smallest]:
                        smallest = j
                input[smallest], input[i] = input[i], input[smallest]
            return input

        tinput = select_sort(tinput)
        return tinput[:k]


solution = Solution()
print(solution.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
