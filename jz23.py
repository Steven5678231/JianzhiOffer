# -*- coding:utf-8 -*-

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == None or len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        length = len(sequence)
        root = sequence[length-1]
        print("root: ", root)
        for i in range(length-1, -1, -1):
            if sequence[i] < root:
                break
        print("i", i)
        for j in range(0, i):
            if sequence[j] > root:
                return False

        left = True
        right = True
        print("left sequence", sequence[0:i+1])
        print("right sequence", sequence[i:length-1])
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i+1])

        if i < length-1:
            right = self.VerifySquenceOfBST(sequence[i:length-1])

        print("left", left)
        print("right", right)
        return left and right


solution = Solution()
print(solution.VerifySquenceOfBST([7, 4, 9, 3, 8, 11, 12, 10]))

# 利用特性找根结点，利用左子树永远小于根结点

# class Solution:
#     def VerifySquenceOfBST(self, sequence):
#         # write code here
#         if not sequence:
#             return False
#         #找到跟节点
#         root = sequence[- 1]
#         i = 0
#         #找到左子树和右子树的分界点
#         while i < len(sequence) - 1:
#             if sequence[i] > root:
#                 break
#             i += 1
#         for j in range(i,len(sequence)-1):
#             if sequence[j] < root:
#                 return False
#         left = True
#         right = True
#         if i > 0:
#             left = self.VerifySquenceOfBST(sequence[:i])
#         if i < len(sequence) - 1:
#             right = self.VerifySquenceOfBST(sequence[i:len(sequence) - 1])
#         return left and right
