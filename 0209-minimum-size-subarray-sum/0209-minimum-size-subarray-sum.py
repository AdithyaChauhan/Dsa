class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        L = 0
        R = 0
        minV = len(nums) + 1
        add = nums[R]
        bla = -1
        while R < len(nums):
            if L > R:
                R = L        
                continue

            if add < target:
                R += 1
                if R == len(nums):
                    break
                add += nums[R]
            
            else:
                minV = min(minV, R - L + 1)
                add -= nums[L]
                L += 1

            # elif add > target:
            #     add -= nums[L]
            #     L += 1
        
        if minV == len(nums) + 1:
            return 0
        return minV