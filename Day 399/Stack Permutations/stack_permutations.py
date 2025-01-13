from typing import List
class Solution:
    def isStackPermutation(self, N : int, A : List[int], B : List[int]) -> int:
        stack=[]
        j=0
        rem_list=[]
        for i in range(N):
            if A[i]==B[j]:
                j+=1
            else:
                if stack!=[] and B[j]==stack[-1]:
                    stack.pop()
                    j+=1
                else:
                    stack.append(A[i])
        if stack!=[] and j<N:
            p=j
            while p<N and stack!=[]:
                if stack[-1]==B[p]:
                    stack.pop()
                    p+=1
                else:
                    rem_list.append(B[p])
                    p+=1
        if stack==[]:
            return 1
        return 0