class Solution:
    def zigzag(self, head_node):
        if head_node is None or head_node.next is None:
            return head_Node
            
        temp = head_node
        flag = False
        
        while temp.next:
            
            if flag:
                if temp.data < temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next
                flag = False 
            else:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next
                flag = True
                
        return head_node