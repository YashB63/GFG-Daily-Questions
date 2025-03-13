import heapq

class Solution:
    def maximizeArray(self, arr1, arr2, n):
        arr=arr1+arr2
        heapq._heapify_max(arr)
        maxArr={}
        ele_count=0
        while ele_count<n:
            if len(arr)>0:
                x=heapq._heappop_max(arr)
            else:
                break
            if x not in maxArr:
                maxArr[x]=1
                ele_count+=1
       
        li=[]
        for ele in arr2:
            if maxArr.get(ele,0)>0:
                maxArr[ele]=0
                li.append(ele)
        for ele in arr1:
            if maxArr.get(ele,0)>0:
                maxArr[ele]=0
                li.append(ele)
     
        return li