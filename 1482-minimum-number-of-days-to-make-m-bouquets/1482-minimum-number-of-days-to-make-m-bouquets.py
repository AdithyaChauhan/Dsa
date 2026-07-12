class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        start = min(bloomDay)
        end = max(bloomDay)
        minV = end
        if m*k > len(bloomDay):
            return - 1
        while start <= end:
            count = 0
            x = 0
            mid = start + (end - start) // 2
            for num in bloomDay:
                if num <= mid:
                    count += 1
                    if count % k == 0:
                        x += 1
                else:
                    count = 0
            if x >= m:
                end = mid - 1
                if m <= x:
                    minV = min(minV, mid)
            else:
                start = mid + 1
        
        return minV