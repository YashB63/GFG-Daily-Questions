class Solution:
    def decodedString(self, s):
        curNum = 0
        stack = []
        curStr = ""
        for i in s:
            if i.isdigit():
                curNum = curNum*10 + int(i)
            elif i == '[' :
                stack.append(curStr) 
                stack.append(curNum)
                curStr = ""
                curNum=0
            elif i == ']' :
                num = stack.pop()
                prevS = stack.pop()
                curStr = prevS + num*curStr
            else : 
                curStr += i
        return curStr