class Solution:
    def decodedString(self, s):
        st = []

        for i in range(len(s)):
            if s[i] != ']':
                st.append(s[i])
            else:
                temp = []

                while st and st[-1] != '[':
                    temp.append(st.pop())
                temp.reverse()  
                st.pop()
                num = []
                
                while st and st[-1].isdigit():
                    num.insert(0, st.pop())

                number = int("".join(num))
                repeat = "".join(
                    temp
                ) * number  

                st.extend(repeat)

        return "".join(st)