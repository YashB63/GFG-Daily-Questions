class Solution:
    def findAnagrams(self, head, str):
        ans=[]
        if not head:
            return ans
        S=sorted(s)
        m=len(s)
        left=head
        right=head
        cur=''
        while right:
            cur+=right.data
            while left!=right and len(cur)>m:
                left=left.next
                cur=cur[1:]
            if sorted(cur)==S:
                ans.append(left)
                tmp=right.next
                right.next=None
                left=tmp
                right=tmp
                cur=''
            else:
                right=right.next
        return ans