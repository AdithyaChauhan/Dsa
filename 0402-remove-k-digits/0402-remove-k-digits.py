class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        st = []

        for si in range(len(num)):
            
            while st and num[si] < st[-1] and k > 0:
                st.pop()
                k -= 1
            
           
            st.append(num[si])
        
        if k > 0:
            st = st[:-k]
        
        ans =  "".join(st).lstrip('0')
        if ans:return ans
        else: return "0"