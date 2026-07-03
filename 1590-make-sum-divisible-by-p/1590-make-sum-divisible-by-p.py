class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0

        n = len(nums)
        seen = {0: -1}
        
        curr = 0
        minLen = n
    
        for i in range(n):
            curr = (curr + nums[i]) % p
            looking_for = (curr - need) % p
            if looking_for in seen:
                minLen = min(minLen, i - seen[looking_for])
            seen[curr] = i

        return minLen if minLen < n else -1