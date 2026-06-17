class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        seen = set()
        count = 0
        for c in jewels:
            if c not in seen:
                seen.add(c)
        
        for x in stones:
            if x in seen:
                count += 1

        return count