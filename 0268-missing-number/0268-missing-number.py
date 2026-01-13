class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = (n * (n+1)) //2 
        sum2 = 0
        for i in range(n):
            sum2 += nums[i]
        if sum2 > sum1:
            return sum2 - sum1
        else: 
            return sum1 - sum2