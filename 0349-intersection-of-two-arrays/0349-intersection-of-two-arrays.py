class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        h = set()
        x = set()

        n1 = len(nums1)
        n2 = len(nums2)

        def create_set(nums, h):
            for i in range(len(nums)):
                h.add(nums[i])

        
        def itera(h, num,x):
            for i in range(len(num)):
                if num[i] in h:
                    x.add(num[i])
                    
        if n1 > n2:
            create_set(nums1, h)
            itera(h, nums2, x)
        else:
            create_set(nums2, h)
            itera(h, nums1,x)
        
        return list(x)