class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        yrs = [0]*101

        for b, d in logs:
            yrs[b-1950] += 1
            yrs[d-1950] -= 1
        
        curr = 0
        best = 0
        best_yr = 0

        for i in range(101):
            curr += yrs[i]

            if curr > best:
                best = curr
                best_yr = i + 1950
        
        return best_yr