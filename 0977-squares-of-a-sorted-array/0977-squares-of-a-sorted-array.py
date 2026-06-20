class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        x = 0
        n = len(nums)
        ans= []

        while x < n:
            if nums[x] >= 0:
                break
            x += 1
        neg = x -1
        pos = x
        for i in range(n):
            nums[i] = nums[i]**2
        while neg >= 0 and pos < n:
            if nums[neg] > nums[pos]:
                ans.append(nums[pos])
                pos += 1
            else:
                ans.append(nums[neg])
                neg -= 1
        
        while neg >= 0:
            ans.append(nums[neg])
            neg -= 1

        while pos < n:
            ans.append(nums[pos])
            pos += 1
            
        return ans