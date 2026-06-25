class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}
        n = len(s)
        R = 0
        L = 0
        maxV = 0
        maxfrq = 0
        for R in range(0, n):

            seen[s[R]] = seen.get(s[R], 0) + 1
            maxfrq = max(maxfrq, seen[s[R]])

            if (R - L + 1) - maxfrq <= k:
                maxV = max(maxV, R - L + 1)
            else:
                seen[s[L]] = seen.get(s[L], 0) - 1
                L += 1

        print(seen)
        return maxV