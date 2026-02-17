class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lb = n  # Default: insert at end if target > all elements
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] >= target:
                # Potential answer found, but check left for earlier position
                lb = mid
                high = mid - 1
            else:
                # nums[mid] < target, need larger values
                low = mid + 1
        
        return lb