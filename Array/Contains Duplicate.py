# ret true if val appears at least twice in the array

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #mem effectent
        # prevVal = None
        # for val in sorted(nums):
        #     if prevVal == val:
        #         return True
        #     prevVal = val
        # return False

        #fast
        return len(nums) != len(set(nums))

assert Solution().containsDuplicate([1,2,3,1]) == True
assert Solution().containsDuplicate([1,2,3,4]) == False