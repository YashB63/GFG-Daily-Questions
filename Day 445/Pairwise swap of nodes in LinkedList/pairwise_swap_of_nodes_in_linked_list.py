def pairwiseSwap(head):
    if (head is None or head.next is None):
        return head

    prevNode = head
    currNode = head.next

    head = currNode

    while True:
        nextNode = currNode.next
         
        currNode.next = prevNode  

        if (nextNode is None or nextNode.next is None):
            prevNode.next = nextNode
            break

        prevNode.next = nextNode.next

        prevNode = nextNode
        currNode = prevNode.next
        
    return head