class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = {'(':')', '{':'}', '[': ']'}
        for ch in s:
            if ch in dic:
                st.append(ch) 
            else:
                if not st:
                    return False
                top = st.pop()
                if ch != dic[top]:
                    return False
        if st:
            return False
        return True