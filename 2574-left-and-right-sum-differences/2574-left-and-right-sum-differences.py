class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        add = 0
        for num in nums:
            add += num
        left = 0
        ans = []
        for i in range(len(nums)):
            add -= nums[i]
            ans.append(abs(add - left))
            left += nums[i]
        return ans