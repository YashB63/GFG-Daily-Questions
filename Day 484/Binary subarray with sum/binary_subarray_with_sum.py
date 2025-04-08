class Solution:
    def numberOfSubarrays(self, arr, target):
        def count(goal):
            i=j=0
            c=s=0
            while j<len(arr):
                s+=arr[j]
                while(s>goal):
                    s-=arr[i]
                    i+=1
                c+=(j-i+1)
                j+=1
            return c
        return count(target)-count(target-1)