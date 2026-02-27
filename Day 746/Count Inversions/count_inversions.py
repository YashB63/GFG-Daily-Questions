class Solution:
    def inversionCount(self, arr):
        def sort_count(a):
            if len(a)<=1:
                return a,0
            mid=len(a)//2
            left, x=sort_count(a[:mid])
            right,y=sort_count(a[mid:])
            i=j=inv=0
            res = []
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    res.append(left[i])
                    i+=1
                    
                else:
                   res.append(right[j])
                   inv += len(left) - i
                   j+=1
            return res + left[i:] + right[j:], x+y+inv
            
        return sort_count(arr)[1]