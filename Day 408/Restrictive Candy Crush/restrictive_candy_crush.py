class Solution:
    def Reduced_String(self, k, s):
        st=[]
        if k==1:
            return ''
        for i in s:
            if not st or st[-1][0]!=i:
                st.append((i,1))
            else:
                st[-1]=(st[-1][0],st[-1][1]+1)
                if st[-1][1]==k:
                    st.pop()
        return ''.join(ch*cnt for ch,cnt in st)