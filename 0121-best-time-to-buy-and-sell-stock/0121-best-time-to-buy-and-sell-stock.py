class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        n = len(nums)
        minV = nums[0]

        profit = 0

        for i in range(1, n):

            minV = min(minV, nums[i])

            profit = max (profit, nums[i] - minV)

        
        return profit