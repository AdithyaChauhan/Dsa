class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        pref_sum = 0
        pref_count = {0:1}
        count = 0
        for num in nums:
            pref_sum += num

            if pref_sum % k in pref_count:
                count += pref_count[pref_sum % k]
            
            pref_count[pref_sum % k] = pref_count.get(pref_sum % k, 0) + 1
        
        return count