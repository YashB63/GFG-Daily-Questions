class Solution:
    
    def InfixtoPostfix(self, exp):
        #code here
        def prec(p):
            if p=='^':
                return 3
            elif p=='*' or p=='/':
                return 2
            elif p=='+' or p=='-':
                return 1
            else:
                return -1
        st=[]
        res=''
        for i in range(len(exp)):
            c=exp[i]
            if c=='(':
                st.append(c)
            elif c==')':
                while st[-1]!='(':
                    res+=st[-1]
                    st.pop()
                st.pop()
            elif 65<=ord(c)<=90 or 97<=ord(c)<=122 or 48<=ord(c)<=57:
                res+=c
            else:
                while len(st)!=0 and prec(c)<=prec(st[-1]):
                    res+=st[-1]
                    st.pop()
                st.append(c)
        while len(st)!=0:
            res+=st[-1]
            st.pop()
        return res