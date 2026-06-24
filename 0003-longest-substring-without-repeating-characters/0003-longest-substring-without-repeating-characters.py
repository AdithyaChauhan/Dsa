class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        maxV = 0
        L = 0
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                maxV = max(maxV, len(seen))
            else:
                maxV = max(maxV, len(seen))
                while ch in seen:
                    seen.remove(s[L])
                    L += 1
                seen.add(ch)
        
        return maxV