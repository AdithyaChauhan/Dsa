class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        h = set(nums1)
        result = []

        for num in set(nums2):
            if num in h:
                result.append(num)

        return result
