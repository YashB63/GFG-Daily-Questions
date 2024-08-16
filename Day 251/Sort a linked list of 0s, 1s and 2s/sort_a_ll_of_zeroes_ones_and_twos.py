class Solution:
    def segregate(self, head):
        last=head
        lst=[]
        while last!=None:
            lst.append(last.data)
            last=last.next
        lst.sort()
        i=0
        first=head
        while first!=None:
            first.data=lst[i]
            i+=1
            first=first.next
        return head