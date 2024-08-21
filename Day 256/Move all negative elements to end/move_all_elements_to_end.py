class Solution:
    def segregateElements(self, arr):
        pos = []
        neg = []
        for i in range(len(arr)):
            if arr[i] <0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])
        arr.clear()
        arr.extend(pos)
        arr.extend(neg)
        return arr