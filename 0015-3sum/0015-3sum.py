class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            low = i + 1
            end = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while low < end:
                
                if nums[low] + nums[end] == - nums[i]:
                    ans.append([nums[i],nums[low], nums[end]])
                    low += 1
                    end -= 1
                    while low < end and nums[low] == nums[low - 1]:
                        low += 1

                    while low < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif nums[low] + nums[end] > - nums[i]:
                    end -= 1
                else:
                    low += 1

        return ans