class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        pref_count = {0:1}
        pref_sum = 0
        count = 0

        for i in range(len(nums)):
            pref_sum += nums[i]

            if pref_sum - goal in pref_count:
                count += pref_count[pref_sum - goal]
            
            pref_count[pref_sum] = pref_count.get(pref_sum, 0) + 1
        
        return count