class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # st = []

        # for c in tokens:
        #     if c == "+":
        #         st.append(st.pop() + st.pop())
        #     elif c == "-":
        #         second, first = st.pop(), st.pop()
        #         st.append(first - second)
        #     elif c == "*":
        #         st.append(st.pop() * st.pop())
        #     elif c == "/":
        #         second, first = st.pop(), st.pop()
        #         st.append(int(first / second))                
        #     else:
        #         st.append(int(c))
        
        # return st[0]
        def add():
            return stack.pop() + stack.pop()
        def sub():
            return - stack.pop() + stack.pop()
        def mult():
            return stack.pop() * stack.pop()
        def div():
            x = stack.pop()
            return int(stack.pop() /x)
        
        stack = []

        for ch in tokens:
            if ch == "+":
                stack.append(add())
            elif ch == "-":
                stack.append(sub())
            elif ch == "/":
                stack.append(div())
            elif ch == "*":
                stack.append(mult())
            else:
                stack.append(int(ch))
        
        return stack[0]