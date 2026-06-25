class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
                
        if len(p) >  len(s):
            return []

        seen1 = {}
        seen2 = {}
        ans = []
        for ch in p:
            seen1[ch] = seen1.get(ch, 0) + 1
            
        for i in range(len(p)):
            seen2[s[i]] = seen2.get(s[i], 0) + 1
        if seen1 == seen2:
            ans.append(0)

        L = 1
        R = L + len(p) - 1

        while R < len(s):
            seen2[s[L - 1]] -= 1
            if seen2[s[L - 1]] == 0:
                del seen2[s[L - 1]]
            seen2[s[R]] = seen2.get(s[R], 0) + 1
            if seen1 == seen2:
                ans.append(L)
            L += 1
            R += 1
        
        return ans