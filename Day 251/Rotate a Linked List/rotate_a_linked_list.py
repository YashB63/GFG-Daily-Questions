class Solution:
    def rotate(self, head, k):
        arr = []
        while head:
            arr.append(head.data)
            head = head.next
        x = len(arr)
        res= [0]*x
        for i in range(x):
            res[(i-k)%x] = arr[i]
        for i in res:
            print(i,end=" ")