class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        maximum_point=0
        for price in prices:
            min_price=min(min_price,price)
            current_profit=price-min_price
            maximum_point=max(maximum_point,current_profit)
        return maximum_point