class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s_dict = {}

        for a in s:
            s_dict[a] = s_dict.get(a,0) + 1
        
        for b in t:
            if b not in s_dict or s_dict[b] ==0:
                return b
            else:
                s_dict[b] -= 1
        return ''