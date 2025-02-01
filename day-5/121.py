class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # first attempt
        profit = 0
        for x in range(len(prices)):
            for i in range(x, len(prices)):
                if prices[i] - prices[x] > profit:
                    buy = prices[x]
                    sell = prices[i]
                    profit = sell - buy  
        return profit
    # this solution works but is inefficient

    def improved_max_profit(self, prices):
        min_price = float('inf')  # Track the lowest price seen so far
        max_profit = 0  # Track the maximum profit

        for price in prices:
            if price < min_price:
                min_price = price 
                # Update min price if we find a lower one
            else:
                max_profit = max(max_profit, price - min_price)  
                # Update profit if selling at this price is better
        return max_profit
