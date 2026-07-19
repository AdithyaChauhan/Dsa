class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st = []
        n = len(nums)
        ans =[-1]*n

        for i in range(2*n):
            idx = i % n
            while st and nums[idx] > nums[st[-1]]:
                ans[st[-1]] = nums[idx]
                st.pop()
            
            if i < n:
                st.append(i)
        return ans