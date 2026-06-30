class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        pref_sum = 0
        pref_count = {0: -1}
        count = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            if pref_sum % k in pref_count:
                
                if i - pref_count[pref_sum % k] >= 2:
                    return True
            
            if pref_sum % k not in pref_count:
                pref_count[pref_sum % k] = i
                
        return False