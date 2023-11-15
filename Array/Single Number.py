# find the pairless number in an array
# linear runtime complexity
# constant space complexity

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #fast
        x = {}
        
        for val in nums:
            if val in x:
                x[val] += 1
            else:
                x[val] = 1

        return list(x.keys())[list(x.values()).index(1)]


assert Solution().singleNumber([1,2,3,1]) == 2