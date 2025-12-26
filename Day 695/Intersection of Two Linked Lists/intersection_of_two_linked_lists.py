class Solution:
    def findIntersection(self, head1, head2):
        l=[False]*int(1e5+1)
        s=head2
        while(s):
            l[s.data]=True
            s=s.next
        s=head1
        ans=Node(-1)
        p=ans
        while(s):
            if(l[s.data]):
                p.next=Node(s.data)
                p=p.next
            s=s.next
        return ans.next