class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_price=0
        maximum_profit=0
        for price in prices:
            min_price=min(min_price,price)
            current_profit=price-min_price
            maximum_profit=max(current_profit,maximum_profit)
        return maximum_profit