class Solution:

    def decodeIt(self, Str, k):
        # code here
        stack = [""]
        string = ""
        ind = 0

        while ind < len(Str):
            if Str[ind].isalpha():
                stack[-1] += Str[ind]
            else:
                string1 = stack.pop()
                stack.append(string1 * int(Str[ind]))
            
            ind += 1
        
        return "".join(stack)[k - 1]