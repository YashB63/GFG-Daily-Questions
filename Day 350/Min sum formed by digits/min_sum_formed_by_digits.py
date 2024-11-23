class Solution:
    def minSum(self, arr, n):
        if len(arr)==1:
            return arr[0]
        arr.sort()
        sm1=''
        sm2=''
        for i in range(len(arr)):
            if i%2==0:
                sm1+=str(arr[i])
            else:
                sm2+=str(arr[i])
        return int(sm1)+int(sm2)