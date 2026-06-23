class Solution:
    def trap(self, nums: List[int]) -> int:
        
        leftMax = 0
        rightMax = 0
        n = len(nums)
        start = 0
        end = n - 1
        ans = 0

        while start < end:
            leftMax = max(leftMax, nums[start])
            rightMax = max(rightMax, nums[end])

            if leftMax < rightMax:
                ans += leftMax - nums[start]
                start += 1
            else:
                ans += rightMax - nums[end]
                end -= 1        

        return ans