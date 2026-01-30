class Solution:
    # Function to push an element into the stack.
    def insert(self, s, x):
       #code here 
       s.append(x)

    # Function to remove top element from stack.
    def remove(self, s):
        s.pop()
    # Function to print the top element of stack.
    def headOf_Stack(self, s):
        #code here 
        print(s[-1])
    # Function to search an element in the stack.
    def find(self, s, val):
        #code here 
        for i in s:
            if i == val:
                return True
        return False