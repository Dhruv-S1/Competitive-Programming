class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = prices[len(prices)-1] - fee
        sell = 0
        for i in range(len(prices) - 2, -1, -1):
            prev_buy = buy;
            buy = max(prices[i] + sell - fee, buy)
            sell = max(prev_buy - prices[i], sell)
        return sell
            
        
