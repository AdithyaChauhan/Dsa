class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        dice = set()
        count = 0
        max_val = -1

        for i in range(n):
            dice.add(nums[i])
        
        for num in dice:
            k = num
            if k - 1 in dice:
                continue
            while k + 1 in dice:
                count += 1
                k = k + 1
            max_val = max(count, max_val)
            count = 0
        return max_val + 1