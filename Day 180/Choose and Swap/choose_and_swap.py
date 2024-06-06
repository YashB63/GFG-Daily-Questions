class Solution:
    def chooseandswap (self, A):
        
        arr=list(A)
        st=sorted(set(arr))
        seen=set()
        i=0
        j=0
        while i<len(arr):
            seen.add(arr[i])
            while j<len(st) and st[j] in seen: j+=1
            if j>=len(st): break
            if arr[i]>st[j]:
                y = arr[i]
                for x in range(i,len(arr)):
                    if arr[x] == y: arr[x] = st[j]
                    elif arr[x] == st[j]: arr[x] = y
                break
            i+=1
        return "".join(arr)