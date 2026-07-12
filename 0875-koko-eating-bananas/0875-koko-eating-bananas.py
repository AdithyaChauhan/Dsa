class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 1
        end = max(piles)
        ans = end
        while start <= end:
            mid = (start + end) // 2

            count = 0
            for pile in piles:
                if pile % mid == 0:
                    count += pile // mid
                else:
                    count += (pile // mid) + 1

                # ban = ban - mid
                # if ban <= 0:
                #     i += 1
                #     if i < len(piles):
                #         ban = piles[i]
                # count+= 1
            if count > h:
                start = mid + 1
            else:
                end = mid - 1
                ans = min(ans, mid)
        
        return ans