class Solution:
    def checkSorted(self, arr):
        count=0
        i=0
        while(i<len(arr)):
            if arr[i]==i+1:
                i+=1
            else:
                arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
                count+=1
            if (count>2):
                return False
        return (count==2 or count==0)