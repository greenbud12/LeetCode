class Solution(object):
    def maxProfit(self, prices):#prices[i] is the price of a given stock on the ith day
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        preVal = prices[0]
        for val in prices[1:]:
            if val > preVal:
                profit += val - preVal
            preVal = val

        return profit

assert Solution().maxProfit([7,1,5,3,6,4]) == 7
assert Solution().maxProfit([1,2,3,4,5]) == 4
assert Solution().maxProfit([7,6,4,3,1]) == 0
print('All tests passed!')