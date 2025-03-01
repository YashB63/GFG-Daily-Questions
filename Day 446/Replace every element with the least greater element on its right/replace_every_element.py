from typing import List

class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        lst = [arr[-1]]
        ans = [-1]*len(arr)
        for i in range(n-2,-1,-1):
            if lst[-1] < arr[i]:
                lst.append(arr[i])
            else:
                k,add = self.bsearch(lst,arr[i])
                if k < len(lst):
                    ans[i] = lst[k]
                if add:
                    lst.insert(k,arr[i])
        return ans
        
    def bsearch(self,arr,x):
        i = 0
        j = len(arr) -1
        while i<=j:
            mid = (i+j)//2
            if arr[mid] == x:
                return mid+1,False
            if arr[mid] < x:
                i = mid +1
            else: 
                j = mid - 1
        return i , True