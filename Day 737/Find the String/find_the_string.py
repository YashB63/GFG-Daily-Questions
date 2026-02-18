class Solution:
    def findString(self, N, K):
        total=K**N
        
        def construct(strn,curr,st):
            if curr==total:
                return ""
            lstStr=strn[1:]
            ans="PP"
            for i in range(K):
                newStr=lstStr+str(i)
                if newStr not in st:
                    st.add(newStr)
                    tmp=construct(newStr,curr+1,st)
                    st.remove(newStr)
                    if tmp!="PP":
                        return str(i)+tmp
            return ans
        
        strVal="0"*N
        st=set()
        st.add(strVal)
        ans=construct(strVal,1,st)
        return strVal+ans