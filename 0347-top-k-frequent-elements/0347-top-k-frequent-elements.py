class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_nums = {}
        ans = []
        for i in range(len(nums)):
            count_nums[nums[i]] = count_nums.get(nums[i], 0) + 1
        
        sorted_nums = sorted(count_nums, key=count_nums.get, reverse=True)

        for i in range(k):

            ans.append(sorted_nums[i])
        
        return ans