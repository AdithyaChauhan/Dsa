class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        goal = 0
        see = {0:-1}
        pref_sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pref_sum += - 1
            else:
                pref_sum += 1
        
            if pref_sum - goal in see:
                ans = max(ans, i - see[pref_sum - goal])
            
            if pref_sum not in see:
                see[pref_sum] = i
        
        return ans