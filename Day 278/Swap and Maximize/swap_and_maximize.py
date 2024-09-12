class Solution:
    def maxSum(self,arr):
        if len(arr)==1:
            return 0
        arr1=sorted(arr)
        arr2=sorted(arr,reverse=True)
        arr3=[]
        sum1=0
        for i in range (len(arr)//2):
            arr3.append(arr1[i])
            arr3.append(arr2[i])
        if len(arr)%2!=0:
            arr3.append(arr1[(len(arr)//2)+1])
        for i in range (len(arr3)-1):
            sum1+=abs(arr3[i]-arr3[i+1])
        sum1+=abs(arr3[0]-arr3[len(arr3)-1])
        return sum1