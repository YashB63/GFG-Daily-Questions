class Solution:
    def removeAdj(self, arr):
        stk = []  
        n = len(arr)

        for e in arr:
            if stk and stk[-1] == e:
                stk.pop()
            else:
                stk.append(e)

        return len(stk)