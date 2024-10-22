class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = prices[0], prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                high = prices[i]
            else:
                res += (high - low)
                low, high = prices[i], prices[i]
        return res + high - low