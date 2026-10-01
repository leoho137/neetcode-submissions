class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        for p in range(len(prices) - 1):
            if prices[p] < prices[buy]:
                buy = p
            sell = p + 1

            print(buy, sell)
            profit = max(profit, prices[sell] - prices[buy])
        return profit