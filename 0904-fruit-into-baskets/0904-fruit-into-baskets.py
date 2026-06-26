class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
 
        L = 0
        R = 0
        seen = {}
        ans = 0
        while R < len(fruits):

            seen[fruits[R]] = seen.get(fruits[R], 0) + 1
            while len(seen) == 3:
                seen[fruits[L]] -= 1
                if seen[fruits[L]] == 0:
                    seen.pop(fruits[L])
                L += 1
            ans = max(ans, R- L + 1)
            R += 1

        return ans