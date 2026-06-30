class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alt = 0
        si = 0
        for num in gain:
            si += num
            alt = max(si, alt)

        return alt