class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for c in tokens:
            if c == "+":
                st.append(st.pop() + st.pop())
            elif c == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))                
            else:
                st.append(int(c))
        
        return st[0]
        # def add(tokens):
        #     return stack.pop() + stack.pop()
        # def sub(tokens):
        #     return - stack.pop() + stack.pop()
        # def mult(tokens):
        #     return stack.pop() * stack.pop()
        # def div(tokens):
        #     x = stack.pop()
        #     return stack.pop() //x
        
        # stack = []

        # for ch in tokens:
        #     if ch == "+":
        #         stack.append(add(tokens))
        #     elif ch == "-":
        #         stack.append(sub(tokens))
        #     elif ch == "/":
        #         stack.append(div(tokens))
        #     elif ch == "*":
        #         stack.append(mult(tokens))
        #     else:
        #         stack.append(int(ch))
        
        # return stack[0]