
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def mergeResult(self, h1, h2):
        
        x = []
        while h1:
            x.append(h1.data)
            h1 = h1.next
            
        while h2:
            x.append(h2.data)
            h2 = h2.next
            
        x.sort(reverse = True)
        node = Node(0)
        temp = node
        for i in x:
            n = Node(i)
            temp.next = n
            temp = temp.next
        
        return node.next

