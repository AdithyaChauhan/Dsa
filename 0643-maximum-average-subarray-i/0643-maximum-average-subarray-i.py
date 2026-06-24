class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        maxV = float('-inf')

        L = 0
        R = k - 1
        window = 0
        for i in range(k):
            window += nums[i]
        maxV = max(maxV, window/k)

        L += 1
        R += 1
        while R < n:
            window = window - nums[L - 1] + nums[R]
            maxV = max(maxV, window/k)
            L += 1
            R += 1
        
        return maxV