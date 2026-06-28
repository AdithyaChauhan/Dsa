class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        L = 0
        zero = 0
        maxV = 0
        haszero = 0
        for R, num in enumerate(nums):

            if num == 0:
                zero += 1
                haszero += 1

            while zero > 1:
                if nums[L] == 0:
                    zero -= 1
                L += 1
            maxV = max(maxV, R-L+1-zero)

        if haszero:
            return maxV
        return maxV - 1