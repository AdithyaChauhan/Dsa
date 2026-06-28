class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        L = 0
        zero = 0
        maxV = 0
        n = len(nums)
        for R, num in enumerate(nums):
            
            if num == 0:
                zero += 1

            while zero > k:
                if nums[L] == 0:
                    zero -= 1
                L += 1
            
            maxV = max(maxV, R - L + 1)
        return maxV