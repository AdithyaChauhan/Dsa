class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        has = {}

        for i in range(n):
            comp = target - nums[i]
            if comp in has:
                return [has[comp], i] 
            has[nums[i]] = i
        
        return [-1,-1]