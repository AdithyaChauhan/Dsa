class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        runningSum = []
        add = 0
        for num in nums:
            add += num
            runningSum.append(add)
        
        return runningSum