class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1

        ans = 0

        while low < high:
            ans = max((high - low) * min(height[low],height[high]), ans)

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return ans