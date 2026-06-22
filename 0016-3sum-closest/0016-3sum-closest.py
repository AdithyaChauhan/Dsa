class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        ans = float('inf')
        for i in range(n-2):
            start = i + 1
            end = n-1

            while start < end:
                add = nums[start] + nums[end] + nums[i]
                if add == target:
                    return target
         
                if abs(target - add) < abs(ans - target):
                    ans = add
                if add > target:
                    end -= 1
                else:
                    start += 1
        return ans
