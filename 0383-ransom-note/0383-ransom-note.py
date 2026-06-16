class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        d = {}

        for ch in magazine:
            d[ch] = d.get(ch,0) + 1

        for c in ransomNote:
            if c in d and d[c] > 0:
                d[c] -= 1
            else:
                return False
        
        return True