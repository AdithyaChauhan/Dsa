class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}

        for a in range(len(s)):
            if s[a] not in s_dict:
                s_dict[s[a]] = [a]
            else:
                s_dict[s[a]].append(a)
        
        for b in range(len(t)):
            if t[b] not in t_dict:
                t_dict[t[b]] = [b]
            else:
                t_dict[t[b]].append(b)        
                       
        if list(s_dict.values()) != list(t_dict.values()):
            return False
        
        return True