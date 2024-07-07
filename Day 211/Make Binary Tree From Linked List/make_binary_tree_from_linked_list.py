from collections import deque

#Function to make binary tree from linked list.
def convert(head):
  
    treeNode = Tree(head.data)
    head = head.next
    stack = deque([treeNode])
    rootNode = treeNode
    while len(stack) and head:
        
        treeNode = stack.popleft()
        
        first = head.data
        treeNode.left = Tree(first)
        stack.append(treeNode.left)
        
        if head.next:
            second = head.next.data
            treeNode.right = Tree(second)
            stack.append(treeNode.right)
        
            head = head.next.next
        else:
            head = head.next
        
    return rootNode