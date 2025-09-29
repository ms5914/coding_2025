class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #there are various states in this question
        # these are the states B1 (buy 1), S1 (sell 1), similarly B2, S2 and the first one that is empty
        #for every price point, we wil evaluate all the 4 states

        buy1 = -1*float("inf")
        sell1 = -1*float("inf")
        buy2 = -1*float("inf")
        sell2 = -1*float("inf")
        empty = 0
        max_profit = 0
        for i in range(len(prices)):
            buy1 = max(buy1, -1*prices[i])
            sell1 = max(sell1, prices[i]+buy1)
            buy2 = max(buy2, sell1-prices[i])
            sell2 = max(sell2, prices[i]+buy2)
            max_profit = max(max_profit, sell1, sell2, empty)
        return max_profit



            

            


        