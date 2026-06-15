class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        char_dict = {}

        for i in range(len(s)):
            char_dict[s[i]] = char_dict.get(s[i], 0) + 1

        for j in range(len(t)):
            if t[j] not in char_dict:
                return False
            else:
                char_dict[t[j]] -= 1

        for value in char_dict.values():
            if value != 0:
                return False
        
        return True