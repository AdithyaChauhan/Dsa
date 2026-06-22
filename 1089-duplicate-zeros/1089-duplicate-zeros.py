class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                count += 1

        i = n - 1
        j = i + count

        while count > 0 and i >=0:

            if  j < n:
                nums[j] = nums[i]
            j -= 1
            
            if nums[i] == 0:
                if j < n:
                    nums[j] = nums[i]
                j -= 1
                count -=1
            i -= 1
        return nums