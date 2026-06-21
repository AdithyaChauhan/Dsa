class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:

        nums.sort()

        start = 0
        end = len(nums) - 1
        ans = 0
        while start <= end:
            if nums[start] + nums[end] <= limit:
                start += 1
                end -= 1
            
            else: end-= 1

            ans += 1
        
        return ans