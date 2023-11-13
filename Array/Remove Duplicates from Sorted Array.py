class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) != 0:
            k = 1
            lastNum = nums[0]
        else:
            return 0
        
        for val in nums[1:]: #start from 2nd element
            if val != lastNum: 
                nums[k], lastNum = val, val 
                k += 1

        return k #count of unique
    
assert Solution().removeDuplicates([1,1,2]) == 2
assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
print('All tests passed!')