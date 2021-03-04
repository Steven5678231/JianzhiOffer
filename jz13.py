class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        index = 0
        while (index < len(array)):
            if (array[index] % 2 == 1):
                odd.append(array[index])
            else:
                even.append(array[index])
            index += 1
        return odd + even


solution = Solution()
print(solution.reOrderArray([1, 2, 3, 4]))
