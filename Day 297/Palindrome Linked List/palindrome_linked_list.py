class Solution:
    def isPalindrome(self, head):
        curr,s=head,[]
        while curr:
            s.append(curr.data)
            curr=curr.next 
        return s==s[::-1]