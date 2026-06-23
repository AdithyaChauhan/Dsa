class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        n = len(nums)
        left = 0
        right = n - 1
        mid = 0

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1


            else:
                mid += 1

        return nums