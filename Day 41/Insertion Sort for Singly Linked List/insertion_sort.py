class Solution:
    def insertionSort(self, head):
       
        curr = head
        arr = []
        while curr:
            arr.append(curr.data)
            curr=curr.next
            
        arr.sort()
        
        assign = head
        
        count = 0
        while assign:
            assign.data = arr[count]
            count += 1
            assign = assign.next
            
        return head