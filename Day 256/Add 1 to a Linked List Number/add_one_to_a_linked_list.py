class Solution:
    def addOne(self,head):
        l = []
        t = head
        while t :
            l.append(t.data)
            t = t.next
        carry = 1
        while l :
            a = l.pop()
            a += carry
            carry = a//10
            a%=10
            newNode = Node(a)
            newNode.next = t
            t = newNode
        if carry != 0 :
            newNode = Node(carry)
            newNode.next = t
            t = newNode
        
        return t