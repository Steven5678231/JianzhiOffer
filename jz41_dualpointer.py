class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        head = 1
        tail = 2
        res = []
        while (head < tail):
            tmp = (head + tail)*(tail - head + 1)/2
            print(head, tail, tmp)
            if (tmp == tsum):
                tmpres = []
                for i in range(head, tail+1):
                    tmpres.append(i)
                res.append(tmpres)
                head += 1
            elif (tmp < tsum):
                tail += 1
            else:
                head += 1
        return res


solution = Solution()
print(solution.FindContinuousSequence(9))
