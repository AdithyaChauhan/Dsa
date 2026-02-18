class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lastOccurence(nums, target):

            start = 0
            end = len(nums) - 1

            while start <= end:

                mid = (start + end) // 2

                if nums[mid] == target:
                    if mid + 1 < len(nums) and nums[mid + 1] == target:
                        start = mid + 1
                    else:
                        return mid

                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return -1

        def firstOccurence(nums, target):

            start = 0
            end = len(nums) - 1

            while start <= end:

                mid = (start + end) // 2

                if nums[mid] == target:
                    if mid - 1  >=0 and nums[mid - 1] == target:
                        end = mid - 1
                    else:
                        return mid

                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return -1

        ans = []
        ans.append(firstOccurence(nums, target))
        ans.append(lastOccurence(nums, target))

        return ans