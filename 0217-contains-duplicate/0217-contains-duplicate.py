class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)
        seen = {}

        for i in range(n):
            if nums[i] not in seen:
                seen[nums[i]] = i
            
            else:
                return True

        return False