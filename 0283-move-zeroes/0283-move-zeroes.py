class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        x = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[x] = nums[x], nums[i]
                x += 1