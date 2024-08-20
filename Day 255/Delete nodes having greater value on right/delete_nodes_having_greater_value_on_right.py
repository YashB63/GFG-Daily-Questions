class Solution:
    def compute(self,head):
        st=[]
        itr=head
        while itr:
            k=itr.data
            if st and k<=temp.data:
                temp.next=itr
                temp=temp.next
            elif len(st)==0:
                st.append(itr)
                temp=itr
                
            else:
                it=st[-1]
                if it.data<k:
                    st.pop()
                    st.append(itr)
                else:
                    
                 while it:
                    if it.next.data>=k:
                        it=it.next
                    else:
                        break
                 it.next=itr
                temp.next=itr
                temp=temp.next
            itr=itr.next    
        return st[0]