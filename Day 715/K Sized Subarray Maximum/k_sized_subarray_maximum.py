class Solution:
    def maxOfSubarrays(self, arr, k):
        st=[]
        l=len(arr)
        ans=[0 for _ in range(l-k+1)]
        def pus(st,ele):
            while st and st[-1]<ele:
                st.pop()
            st.append(ele)
            
        def po(st,ele):
            if st and st[0]==ele:
                st.pop(0)
                
        for i in range(k-1):
            pus(st,arr[i])
            
        for i in range(k-1,l):
            pus(st,arr[i])
            ans[i-k+1]=st[0]
            po(st,arr[i-k+1])
        return ans