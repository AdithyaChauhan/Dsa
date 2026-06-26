class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        seen = {}

        for ch in t:
            seen[ch] = seen.get(ch, 0) + 1
        
        n = len(t)

        L = 0
        R = 0
        minV = float('inf')
        ans = ""
        add = 0
        sIndex = -1
        fIndex = -2
        for R in range(len(s)):
            if s[R] in seen:
                if seen[s[R]] > 0:
                    add += 1
                seen[s[R]] -= 1

            while add == n and L <= R:
                if minV > R - L + 1:
                    sIndex = L
                    fIndex = R
                    minV = R - L + 1
                if s[L] in seen:
                    seen[s[L]] += 1
                    if seen[s[L]] > 0:
                        add -= 1
                L += 1
    

        for i in range(sIndex, fIndex + 1):
            ans += s[i]
        return ans