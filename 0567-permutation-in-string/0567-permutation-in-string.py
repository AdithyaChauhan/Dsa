class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        seen1 = {}
        seen2 = {}

        
        for ch in s1:
            seen1[ch] = seen1.get(ch, 0) + 1

        # Build first window
        for i in range(len(s1)):
            seen2[s2[i]] = seen2.get(s2[i], 0) + 1

        if seen1 == seen2:
            return True

        L = 0

        for R in range(len(s1), len(s2)):
            outgoing = s2[L]
            seen2[outgoing] -= 1

            if seen2[outgoing] == 0:
                del seen2[outgoing]
            L += 1

            incoming = s2[R]
            seen2[incoming] = seen2.get(incoming, 0) + 1


            if seen1 == seen2:
                return True
        
        return False