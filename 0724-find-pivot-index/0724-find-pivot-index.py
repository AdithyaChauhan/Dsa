class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        pref = 0
        sum = 0
        n = len(nums)
        for i in range(n):
            sum += nums[i]

        for i in range(n):

            if sum - pref - nums[i] == pref:
                return i

            pref += nums[i]
        return -1