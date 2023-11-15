#rotate array to the right by k steps

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # solution 1
        # k = k%len(nums)
        # x = nums[-k:] + nums[:-k]
        # nums = x

        # solution 2
        k = k % len(nums) 
        nums.reverse() 
        nums[:k] = reversed(nums[:k]) 
        nums[k:] = reversed(nums[k:])

        # solution 3
        # numLen = len(nums)
        # k = k % numLen
        # count = 0
        # start = 0
        # while count < numLen:
        #     current = start
        #     prev = nums[start]
        #     while True:
        #         next_idx = (current + k) % numLen
        #         nums[next_idx], prev = prev, nums[next_idx]
        #         current = next_idx
        #         count += 1
        #         if start == current:
        #             break
        #     start += 1
        

Solution().rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
Solution().rotate([1,2,3,4,5,6,7], 10) == [5,6,7,1,2,3,4]
print('All tests passed!')