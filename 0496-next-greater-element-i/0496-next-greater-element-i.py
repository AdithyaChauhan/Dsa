class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen = {}
        for i in range(len(nums1)):
            seen[nums1[i]] = i
        ans = [-1]*len(nums1)
        st = []
        #Optimal
        for num in nums2:
            while st and num > st[-1]:
                ans[seen[st[-1]]] = num
                st.pop()

            if num not in seen:
                continue
            st.append(num)
        return ans
        #Brute
        # for i in range(len(nums2)-1):
        #     if nums2[i] in seen:
        #         for j in range(i + 1, len(nums2)):
        #             if nums2[j] > nums2[i]:
        #                 ans[seen[nums2[i]]] = nums2[j]
        #                 break
        # return ans