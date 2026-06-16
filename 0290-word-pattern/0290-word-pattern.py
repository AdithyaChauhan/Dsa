class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(words) != len(pattern):
            return False
        p_s = {}
        s_p = {}
        for j in range(len(words)):
            if words[j] not in s_p:
                s_p[words[j]] = pattern[j]
            elif s_p[words[j]] == pattern[j]:
                continue
            else: 
                return False


            if pattern[j] not in p_s:
                p_s[pattern[j]] = words[j]
            elif p_s[pattern[j]] == words[j]:
                continue
            else: 
                return False

        return True