# given two arrays return intersection as an array

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        i = 0
        k = 0
        while i < len(nums1) and k < len(nums2):
            if nums1[i] == nums2[k]:
                i += 1
                k += 1
            elif nums1[i] < nums2[k]:
                nums1.pop(i)
            else:
                k += 1
                if k >= len(nums2):
                    nums1.pop(i)
                    
        return nums1[:i]

assert Solution().intersect([1,2], [1,1]) == [1]
assert Solution().intersect([1,2,2,1], [2,2]) == [2,2]
assert Solution().intersect([4,9,5], [9,4,9,8,4]) == [4,9]
assert Solution().intersect([4,7,9,7,6,7], [5,0,0,6,1,6,2,2,4]) == [4,6]