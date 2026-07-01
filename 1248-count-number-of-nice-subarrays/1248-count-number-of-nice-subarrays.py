class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        pref_count = {0:1}
        pref_sum = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                pref_sum += 1

            if pref_sum - k in pref_count:
                count += pref_count[pref_sum - k]
            
            pref_count[pref_sum] = pref_count.get(pref_sum, 0) + 1
        
        return count