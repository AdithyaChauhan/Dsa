class Solution:
    def findMin(self, nums: List[int]) -> int:

        s = 0
        e = len(nums) - 1
        ans = float('inf')

        while s <= e:
            mid = s + (e-s)//2
            ans = min(nums[mid], ans)
            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid - 1
        
        return ans






        # while low <= high:
        #     mid = (low + high) // 2

        #     if nums[low] <= nums[mid]:
        #         ans = min(ans, nums[low])
        #         low = mid + 1
        #     else:
        #         ans = min(ans, nums[mid])
        #         high = mid - 1

        # return ans