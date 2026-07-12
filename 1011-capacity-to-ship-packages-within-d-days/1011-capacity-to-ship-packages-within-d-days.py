class Solution:
    def shipWithinDays(self, piles: List[int], h: int) -> int:

        start = 0
        end = start
        for num in piles:
            start = max(start,num)
            end += num

        ans = end
        while start <= end:
            mid = (start + end) // 2
            count = 1
            bun = mid
            i = 0
            su = 0
            while i < len(piles):
                
                if piles[i] + su > bun:
                    su = 0
                    count += 1
                su += piles[i]
                i += 1
            if count > h:
                start = mid + 1
            else:
                end = mid - 1
                ans = min(ans, mid)
        
        return ans
                