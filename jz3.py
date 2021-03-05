class Solution:
    arrayList = []
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    def getBack(self, listNode):
        if not listNode:
            return
        self.getBack(listNode.next)
        self.arrayList.append(listNode.val)
        return None

    def printListFromTailToHead(self, listNode):
        # write code here
        self.arrayList = []
        self.getBack(listNode)

        return self.arrayList
